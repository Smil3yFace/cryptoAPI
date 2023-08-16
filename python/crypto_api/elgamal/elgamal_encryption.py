from crypto_api.elgamal.elgamal_data_classes import *
from crypto_api.math_lib.multiplicative_group import MultiplicativeGroup


class ElGamalEncryption:
    @staticmethod
    def key_gen(prime: int, generator: int) -> ElGamalKeyPair:
        group: MultiplicativeGroup = MultiplicativeGroup(prime)
        secret_key: int = group.random_element()
        public_key: int = group.pow_mod(generator, secret_key)

        return ElGamalKeyPair(secret_key, public_key, ElGamalKeyParams(prime, generator))

    @staticmethod
    def enc(other_public_key: int, key_params: ElGamalKeyParams, message: int) -> ElGamalCipherText:
        group: MultiplicativeGroup = MultiplicativeGroup(key_params.prime)

        y: int = group.random_element()
        gy: int = group.pow_mod(key_params.generator, y)

        c2: int = group.mul_mod(
            group.pow_mod(other_public_key, y),
            message
        )

        c1 = gy
        return ElGamalCipherText(c1, c2)

    @staticmethod
    def dec(secrect_key: int, key_params: ElGamalKeyParams, cipherText: ElGamalCipherText) -> int:
        group: MultiplicativeGroup = MultiplicativeGroup(key_params.prime)

        shared_key = group.pow_mod(cipherText.c1, secrect_key)
        inverse_shared_key = group.mul_invert_mod(shared_key)

        return group.mul_mod(cipherText.c2, inverse_shared_key)
