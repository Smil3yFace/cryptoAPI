from crypto_api.math_lib.multiplicative_group import MultiplicativeGroup
from crypto_api.elgamal.elgamal_encryption import ElGamalEncryption
from crypto_api.elgamal.elgamal_data_classes import ElGamalCipherText, ElGamalKeyParams


###TODO: UNDER CONSTRUCTION
class ThresholdElGamalEncryption:

    @staticmethod
    def key_gen(numOfPlayers: int, prime: int, generator: int) -> (int, [int]):
        group: MultiplicativeGroup = MultiplicativeGroup(prime)
        polynom_degree: int = numOfPlayers - 1
        x_coords_of_players: [int] = [x for x in range(0, numOfPlayers + 1)]
        delta: [int] = ThresholdElGamalEncryption.lagrange_coeff(x_coords_of_players)
        pA: [int] = [group.random_element() for x in range(0, numOfPlayers)]

        # Index 0 is reserved for the shared secret
        secret_keys: [int] = [0 for x in range(0, numOfPlayers + 1)]
        for n in range(1, len(x_coords_of_players)):
            for p in range(0, numOfPlayers):
                secret_keys[n] += pA[p] * (x_coords_of_players[n] ^ p)

        secret_keys[0]: [int] = ThresholdElGamalEncryption.calc_shared_secret(secret_keys, delta)
        public_key: int = group.pow_mod(generator, secret_keys[0])
        secret_keys[0] = 0

        return public_key, secret_keys

    @staticmethod
    def enc(other_public_key: int, key_params: ElGamalKeyParams, message: int) -> ElGamalCipherText:
        return ElGamalEncryption.enc(other_public_key, key_params, message)

    @staticmethod
    def dec(secret_keys: [int], delta: [int], key_params: ElGamalKeyParams, ciphertext: ElGamalCipherText) -> int:
        shared_secret: int = ThresholdElGamalEncryption.calc_shared_secret(secret_keys, delta)
        return ElGamalEncryption.dec(shared_secret, key_params, ciphertext)

    @staticmethod
    def calc_shared_secret(private_keys: [int], delta: [int]) -> int:
        shared_secret: int = 0
        for i in range(1, len(delta)):
            shared_secret += delta[i] * private_keys[i]
        return shared_secret

    @staticmethod
    def lagrange_coeff(x_coords: [int]) -> [int]:
        # TODO: Could ends up in math lib
        delta: [int] = [1 for x in range(0, len(x_coords))]
        for i in range(1, len(delta)):
            for j in range(1, len(delta)):
                delta[i] *= (x_coords[0] - x_coords[j]) / (x_coords[i] - x_coords[j])
        return delta
