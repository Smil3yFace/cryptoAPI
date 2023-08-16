class ElGamalKeyParams:
    def __init__(self, prime: int, generator: int) -> None:
        self.__prime: int = prime
        self.__generator: int = generator

    @property
    def prime(self) -> int:
        return self.__prime

    @property
    def generator(self) -> int:
        return self.__generator


class ElGamalKeyPair:
    def __init__(self, secret_key: int, public_key: int, key_params: ElGamalKeyParams) -> None:
        self.__secret_key = secret_key
        self.__public_key = public_key
        self.__key_params = key_params

    @property
    def secret_key(self) -> int:
        return self.__secret_key

    @property
    def public_key(self) -> int:
        return self.__public_key

    @property
    def key_params(self) -> ElGamalKeyParams:
        return self.__key_params


class ElGamalCipherText:
    def __init__(self, c1: int, c2: int) -> None:
        self._c1 = c1
        self._c2 = c2

    @property
    def c1(self) -> int:
        return self._c1

    @property
    def c2(self) -> int:
        return self._c2
