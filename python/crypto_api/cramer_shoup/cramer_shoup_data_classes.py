class CramerShoupKeyParams:
    def __init__(self, prime: int, generator: int):
        self.__prime: int = prime
        self.__generator: int = generator

    @property
    def prime(self) -> int:
        return self.__prime

    @property
    def generator(self) -> int:
        return self.__generator


class CramerShoupSecretKey:
    def __init__(self, alpha: int, x: int, y: int, z: int, z_: int, w: int, w_: int) -> None:
        self.__alpha: int = alpha
        self.__x: int = x
        self.__y: int = y
        self.__z: int = z
        self.__z_: int = z_
        self.__w: int = w
        self.__w_: int = w_

    @property
    def alpha(self) -> int:
        return self.__alpha

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def z(self) -> int:
        return self.__z

    @property
    def z_(self) -> int:
        return self.__z_

    @property
    def w(self) -> int:
        return self.__w

    @property
    def w_(self) -> int:
        return self.__w_


class CramerShoupPublicKey:
    def __init__(self, A: int, B: int, B_: int, generator: int, g_: int, prime: int) -> None:
        self.__A: int = A
        self.__B: int = B
        self.__B_: int = B_
        self.__generator: int = generator
        self.__g_: int = g_
        self.__prime: int = prime

    @property
    def A(self) -> int:
        return self.__A

    @property
    def B(self) -> int:
        return self.__B

    @property
    def B_(self) -> int:
        return self.__B_

    @property
    def generator(self) -> int:
        return self.__generator

    @property
    def g_(self) -> int:
        return self.__g_

    @property
    def prime(self) -> int:
        return self.__prime


class CramerShoupKeyPair:

    def __init__(self, secret_key: CramerShoupSecretKey, public_key: CramerShoupPublicKey, key_params: CramerShoupKeyParams) -> None:
        self.__secret_key = secret_key
        self.__public_key = public_key
        self.__key_params = key_params

    @property
    def secret_key(self) -> CramerShoupSecretKey:
        return self.__secret_key

    @property
    def public_key(self) -> CramerShoupPublicKey:
        return self.__public_key

    @property
    def key_params(self) -> CramerShoupKeyParams:
        return self.__key_params


class CramerShoupCipherText:

    def __init__(self, R: int = 0, R_: int = 0, P: int = 0, T: int = 0):
        self._R: int = R
        self._R_: int = R_
        self._P: int = P
        self._T: int = T

    @property
    def R(self) -> int:
        return self._R

    @property
    def R_(self) -> int:
        return self._R_

    @property
    def P(self) -> int:
        return self._P

    @property
    def T(self) -> int:
        return self._T