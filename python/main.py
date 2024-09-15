from cramer_shoup.cramer_shoup_data_classes import CramerShoupCipherText
from cramer_shoup.cramer_shoup_encryption import CramerShoupEncryption
from crypto_api.math_lib import misc
from diffie_hellman_key_exchange import diffie_hellman_key_exchange
from elgamal import threshold_elgamal_encryption, elgamal_data_classes
from elgamal.elgamal_encryption import ElGamalEncryption
from math_lib.multiplicative_group import MultiplicativeGroup
from rsa.fulldomainhash_rsa_encryption import FullDomainHashRSAEncryption


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def diffie_hellman_example() -> None:
    p: int = misc.gen_prime(10000, 90000)
    g = misc.gen_generator(p)

    dh_alice = diffie_hellman_key_exchange.DiffieHellmanKeyExchange(p, g)
    dh_bob = diffie_hellman_key_exchange.DiffieHellmanKeyExchange(p, g)

    dh_alice.generate_shared_key(dh_bob.public_key)
    dh_bob.generate_shared_key(dh_alice.public_key)

    print("alice: ", dh_alice.to_json_str())
    print("bob: ", dh_bob.to_json_str())


def cramer_shoup_example() -> None:
    alice_prime = misc.gen_prime(0, 330)
    alice_generator = misc.gen_generator(alice_prime)

    bob_prime = misc.gen_prime(330, 621)
    bob_generator = misc.gen_generator(bob_prime)

    alice = CramerShoupEncryption.key_gen(alice_prime, alice_generator)
    bob = CramerShoupEncryption.key_gen(bob_prime, bob_generator)

    m1 = 7983 % bob.key_params.prime
    m2 = 8880 % bob.key_params.prime
    print("m1: ", m1)
    print("m2: ", m2)

    c1 = CramerShoupEncryption.enc(bob.public_key, alice.key_params, m1)
    c2 = CramerShoupEncryption.enc(bob.public_key, alice.key_params, m2)

    print("c1: ", c1)
    print("c2: ", c2)

    dec_m1 = CramerShoupEncryption.dec(bob.secret_key, bob.key_params, c1)
    print("dec m1: ", dec_m1)
    dec_m2 = CramerShoupEncryption.dec(bob.secret_key, bob.key_params, c2)
    print("dec m2: ", dec_m2)

    print("homomorphism - Test")
    c3 = CramerShoupCipherText()
    for attr, value in c1.__dict__.items():
        setattr(
            c3,
            attr,
            MultiplicativeGroup(bob_prime).mul_mod(getattr(c1, attr), getattr(c2, attr))
        )
    print("c3: ", c3)
    dec_m3 = CramerShoupEncryption.dec(bob.secret_key, bob.key_params, c3)
    print("dec m3: ", dec_m3)


def elgamal_example() -> None:
    p = misc.gen_prime(3, 621)
    g = misc.gen_generator(p)

    Bob = ElGamalEncryption.key_gen(p, g)
    Alice = ElGamalEncryption.key_gen(p, g)

    print("Bob keys: ", Bob.public_key, Bob.secret_key)
    print("Alice Key: ", Alice.public_key, Alice.secret_key)

    m = 32
    print("Original Message", m)

    mEnc = ElGamalEncryption.enc(Alice.public_key, Bob.key_params, m)
    print("Encrypted", mEnc.c1, mEnc.c2)

    mDec = ElGamalEncryption.dec(Alice.secret_key, Alice.key_params, mEnc)
    print("Decrypted", mDec)


def threshold_elgamal_example() -> None:
    playerCount = 3
    p = misc.gen_prime(10000, 90000)
    g = misc.gen_generator(p)

    (delta, pKey, sKeys) = threshold_elgamal_encryption.ThresholdElGamalEncryption.key_gen(playerCount, p, g)

    print("Secret Keys: ", sKeys)
    print("Public Key: ", pKey)

    sKey: int = threshold_elgamal_encryption.ThresholdElGamalEncryption.calc_shared_secret(sKeys, delta)
    print("Calculated Secret Key:", sKey)

    m = 2345 % p
    print("Original Message: ", m)

    mEnc = threshold_elgamal_encryption.ThresholdElGamalEncryption.enc(pKey,
                                                                       elgamal_data_classes.ElGamalKeyParams(p, g), m)
    print("Encrypted Message: {", mEnc.c1, ", ", mEnc.c2, "}")

    mDec = threshold_elgamal_encryption.ThresholdElGamalEncryption.dec(sKeys, delta,
                                                                       elgamal_data_classes.ElGamalKeyParams(p, g),
                                                                       mEnc)
    print("Decrypted Message:", mDec)


def fulldomain_rsa_example() -> None:
    p = misc.gen_prime(10000, 90000)
    q = misc.gen_prime(10000, 90000)

    f = FullDomainHashRSAEncryption()
    rsa_keypair = f.key_gen(p, q)
    m = "Hallo"
    sign = f.sign(rsa_keypair.secret_key, m)
    print("Verifikation:", f.verify(rsa_keypair.public_key, m, sign))


if __name__ == "__main__":
    #diffie_hellman_example()
    #cramer_shoup_example()
    #elgamal_example()
    #threshold_elgamal_example()
    fulldomain_rsa_example()