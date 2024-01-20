class RSAKeyTuple:
    def __init__(self, key, modul):
        self.__key = key
        self.__modul = modul

    @property
    def key(self) -> int:
        return self.__key

    @property
    def modul(self) -> int:
        return self.__modul


class RSAKeyPair:
    def __init__(self, secret_key: int, public_key: int, rsa_modul: int) -> None:
        self.__secret_key = RSAKeyTuple(secret_key, rsa_modul)
        self.__public_key = RSAKeyTuple(public_key, rsa_modul)

    @property
    def secret_key(self) -> RSAKeyTuple:
        return self.__secret_key

    @property
    def public_key(self) -> RSAKeyTuple:
        return self.__public_key