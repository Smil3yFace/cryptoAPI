import math_lib.misc
from crypto_api.elgamal.elgamal_data_classes import ElGamalCipherText, ElGamalKeyParams
from crypto_api.elgamal.elgamal_encryption import ElGamalEncryption
from crypto_api.math_lib.multiplicative_group import MultiplicativeGroup


###TODO: UNDER CONSTRUCTION
class ThresholdElGamalEncryption:

    @staticmethod
    def key_gen(numOfPlayers: int, prime: int, generator: int) -> (int, int, [int]):
        group: MultiplicativeGroup = MultiplicativeGroup(prime)
        polynom_degree: int = numOfPlayers - 1
        x_coords_of_players: [int] = [x for x in range(0, numOfPlayers + 1)]
        delta: [int] = math_lib.misc.calc_lagrange_coeff(x_coords_of_players)
        y_coords_of_players: [int] = [group.random_element() for x in range(0, numOfPlayers)]

        # Index 0 is reserved for the shared secret
        secret_keys: [int] = [0 for x in range(0, numOfPlayers + 1)]
        for n in range(1, len(x_coords_of_players)):
            for p in range(0, numOfPlayers):
                secret_keys[n] += y_coords_of_players[p] * (x_coords_of_players[n] ^ p)

        secret_keys[0]: [int] = ThresholdElGamalEncryption.calc_shared_secret(secret_keys, delta)
        public_key: int = group.pow_mod(generator, secret_keys[0])
        secret_keys[0] = 0

        return delta, public_key, secret_keys

    @staticmethod
    def enc(other_public_key: int, key_params: ElGamalKeyParams, message: int) -> ElGamalCipherText:
        return ElGamalEncryption.enc(other_public_key, key_params, message)

    @staticmethod
    def dec(secret_keys: [int], delta: [int], key_params: ElGamalKeyParams, ciphertext: ElGamalCipherText) -> int:
        shared_secret: int = ThresholdElGamalEncryption.calc_shared_secret(secret_keys, delta)
        return ElGamalEncryption.dec(shared_secret, key_params, ciphertext)

    @staticmethod
    def calc_shared_secret(secret_key: [int], delta: [int]) -> int:
        shared_secret: int = 0
        for i in range(1, len(delta)):
            shared_secret += delta[i] * secret_key[i]
        return shared_secret

