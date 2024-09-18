import math
import random

from crypto_api.rsa.rsa_data_classes import *


class RSAEncryption:
    @staticmethod
    def key_gen(p: int, q: int) -> RSAKeyPair:
        N: int = p * q
        phi: int = (p-1) * (q-1)

        e: int = RSAEncryption._sample_e(phi)
        d: int = pow(e, -1, phi)

        # secret key: (e, N)
        # public key: (d, N)
        return RSAKeyPair(e, d, N)

    @staticmethod
    def enc(other_public_key: RSAKeyTuple, message: int) -> int:
        return (message ** other_public_key.key) % other_public_key.modul

    @staticmethod
    def dec(secret_key: RSAKeyTuple, cipher_text: int) -> int:
        return (cipher_text ** secret_key.key) % secret_key.modul


    @staticmethod
    def _sample_e(phi: int) -> int:
        e: int = random.randint(0, phi)
        while e != 1 and math.gcd(e, phi) != 1:
            e = random.randint(0, phi)
        return e
