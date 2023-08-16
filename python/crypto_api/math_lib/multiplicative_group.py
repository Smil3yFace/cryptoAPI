import random

from crypto_api.math_lib.misc import phi, ext_factors


class MultiplicativeGroup:

    def __init__(self, modulo: int) -> None:
        self.__m = modulo
        self.__order = phi(ext_factors(modulo))

    def mul_mod(self, x: int, y: int) -> int:
        return ((x % self.__m) * (y % self.__m)) % self.__m

    def pow_mod(self, base: int, power: int) -> int:
        result = 1
        for i in range(power):
            result = self.mul_mod(result, base)
        return result

    def mul_invert_mod(self, x) -> int:
        return x ** (self.__order - 1) % self.__m

    def random_element(self) -> int:
        return random.randint(0, self.__m - 1)

    @property
    def order(self) -> int:
        return self.__order

    @property
    def modulo(self) -> int:
        return self.__m
