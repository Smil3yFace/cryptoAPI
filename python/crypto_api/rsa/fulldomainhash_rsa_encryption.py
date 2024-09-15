import hashlib

from rsa.rsa_data_classes import RSAKeyTuple
from rsa.rsa_encryption import RSAEncryption


class FullDomainHashRSAEncryption(RSAEncryption):

    @staticmethod
    def sign(secret_key: RSAKeyTuple, message: str) -> int:
        hash_method = hashlib.sha3_512
        h = int(hash_method(message.encode()).hexdigest(), 16)
        return pow(h, secret_key.key, secret_key.modul)

    @staticmethod
    def verify(public_key: RSAKeyTuple, message: str, signature: int) -> bool:
        hash_method = hashlib.sha3_512
        h = int(hash_method(message.encode()).hexdigest(), 16)
        return h % public_key.key == pow(signature, public_key.key, public_key.modul)