import hashlib
import random

from crypto_api.cramer_shoup.cramer_shoup_data_classes import *
from crypto_api.math_lib.multiplicative_group import MultiplicativeGroup


class CramerShoupEncryption:

    @staticmethod
    def key_gen(prime: int, generator: int) -> CramerShoupKeyPair:
        group: MultiplicativeGroup = MultiplicativeGroup(prime)

        key_params: CramerShoupKeyParams = CramerShoupKeyParams(prime, generator)

        secret_key: CramerShoupSecretKey = CramerShoupSecretKey(
            group.random_element(),  # alpha
            group.random_element(),  # x
            group.random_element(),  # y
            group.random_element(),  # z
            group.random_element(),  # z_
            group.random_element(),  # w
            group.random_element()  # w_
        )

        g_: int = group.pow_mod(generator, secret_key.alpha)
        public_key: CramerShoupPublicKey = CramerShoupPublicKey(
            # A
            group.mul_mod(
                group.pow_mod(generator, secret_key.x),
                group.pow_mod(g_, secret_key.y)
            ),
            # B
            group.mul_mod(
                group.pow_mod(generator, secret_key.z),
                group.pow_mod(g_, secret_key.w)
            ),
            # B_
            group.mul_mod(
                group.pow_mod(generator, secret_key.z_),
                group.pow_mod(g_, secret_key.w_)
            ),
            generator,
            g_,
            prime
        )

        return CramerShoupKeyPair(secret_key, public_key, key_params)

    @staticmethod
    def enc(other_public_key: CramerShoupPublicKey, key_params: CramerShoupKeyParams, message: int) -> CramerShoupCipherText:
        group: MultiplicativeGroup = MultiplicativeGroup(other_public_key.prime)

        hash_algo: hashlib.sha3_512 = hashlib.sha3_512()
        r = random.randint(0, key_params.prime - 1)

        R: int = group.pow_mod(other_public_key.generator, r)
        R_: int = group.pow_mod(other_public_key.g_, r)
        P: int = group.mul_mod(group.pow_mod(other_public_key.A, r), message)
        beta: bytes = (str(R_) + str(R) + str(P)).encode()
        hash_algo.update(beta)
        h: int = int(hash_algo.hexdigest(), 16) % group.order
        T = group.pow_mod(
            group.mul_mod(
                other_public_key.B,
                group.pow_mod(other_public_key.B_, h),
            ),
            r
        )
        return CramerShoupCipherText(R, R_, P, T)

    @staticmethod
    def dec(secret_key: CramerShoupSecretKey, key_params: CramerShoupKeyParams, ciphertext: CramerShoupCipherText) -> int:
        group: MultiplicativeGroup = MultiplicativeGroup(key_params.prime)
        hash_algo: hashlib.sha3_512 = hashlib.sha3_512()

        beta_ = (str(ciphertext.R_) + str(ciphertext.R) + str(ciphertext.P)).encode()
        hash_algo.update(beta_)
        h: int = int(hash_algo.hexdigest(), 16) % group.order

        # T validation part 1
        T_val1: int = group.mul_mod(
            group.pow_mod(ciphertext.R, secret_key.z),
            group.pow_mod(ciphertext.R, (h * secret_key.z_) % group.order)
        )

        T_val2: int = group.mul_mod(
            group.pow_mod(ciphertext.R_, secret_key.w),
            group.pow_mod(ciphertext.R_, (h * secret_key.w_) % group.order)
        )

        if ciphertext.T == group.mul_mod(T_val1, T_val2):
            Rx: int = group.pow_mod(ciphertext.R, secret_key.x)
            R_y: int = group.pow_mod(ciphertext.R_, secret_key.y)
            inverse_RxR_y: int = group.mul_invert_mod(group.mul_mod(Rx, R_y))
            return group.mul_mod(ciphertext.P, inverse_RxR_y)
        else:
            raise Exception("Validation error")
