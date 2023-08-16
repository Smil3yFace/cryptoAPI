from random import randint
from crypto_api.math_lib.multiplicative_group import MultiplicativeGroup


class DiffieHellmanKeyExchange:

    def __init__(self, prime: int, generator: int) -> None:
        self.__group = MultiplicativeGroup(prime)

        self.__secret_key = self.__group.random_element()
        self.__public_key = self.__group.pow_mod(generator, self.__secret_key)
        self.__shared_key = 0

    def generate_shared_key(self, other_public_key: int) -> None:
        self.__shared_key = self.__group.pow_mod(other_public_key, self.__secret_key)

    def to_json_str(self) -> str:
        return (
            "{shared_key: %d, public_key: %d, secrect_key: %d}" %
            (self.__shared_key, self.__public_key, self.__secret_key)
        )

    @property
    def shared_key(self) -> int:
        return self.__shared_key

    @property
    def public_key(self) -> int:
        return self.__public_key
