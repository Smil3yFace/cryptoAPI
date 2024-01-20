from crypto_api.math_lib.multiplicative_group import MultiplicativeGroup
from crypto_api.rsa.rsa_data_classes import *

class RSAEncryption:
    @staticmethod
    def key_gen(p: int, q: int) -> RSAKeyPair:
        N: int = p * q
        group: MultiplicativeGroup = MultiplicativeGroup(N)
        phi: int = group.mul_mod((p - 1), (q - 1))

        e: int = RSAEncryption.sample_e(phi)
        d: int = group.mul_invert_mod(e, phi)

        # secret key: (e, N)
        # public key: (d, N)
        return RSAKeyPair(e, d, N)

    @staticmethod
    def enc(other_public_key: RSAKeyTuple, message: int) -> int:
        return 0

    @staticmethod
    def dec(private_key: RSAKeyTuple, cipherText) -> int:
        return 0

    @staticmethod
    def sample_e(phi: int) -> int:
        e: int = 0
        return e
