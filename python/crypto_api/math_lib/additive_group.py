class AdditiveGroup:
    def __init__(self, modulo: int):
        self.__m = modulo

    def add_mod(self, x: int, y: int) -> int:
        return ((x % self.__m) + (y % self.__m)) % self.__m

    def sub_mod(self, x: int, y: int) -> int:
        return self.add_mod(x, self.additive_inverse(y))

    def additive_inverse(self, x: int) -> int:
        return (-x + self.__m) % self.__m

    def pow_mod(self, base: int, power: int) -> int:
        result: int = 0
        for i in range(power):
            result = self.add_mod(result, base)
        return result

    # Order is the number of elements, if H is a group by definition each element is invertible
    # so we count the number of elements
    @property
    def order(self) -> int:
        return self.__m

    @property
    def modulo(self) -> int:
        return self.__m
