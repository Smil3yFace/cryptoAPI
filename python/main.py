from crypto_api.math_lib import misc
from crypto_api.cramer_shoup import cramer_shoup_encryption
from crypto_api.elgamal import elgamal_encryption

def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
# h = c.H()
# g = c.G()

# print(h.add_mod(2,3,6))
# print(g.pow_mod(2,3,10))
# print(c.factors(8))
# print(c.ext_factors(12))
# print(c.phi(c.ext_factors(6)))
# print(g.order(9))
# print(g.mul_invert_mod(2, 5))
# print(test.order(mod))
# print(len(set([test.pow_mod(g, x, mod) for x in range(mod)])))

# mod = 877
# order = c.G().order(mod)
# g = c.gen_generator(mod)

# print(g)
# q = set([c.G().pow_mod(g, y, mod) for y in range(mod)])
# print(len(q), order, q)

# for x in range(1, mod):
#     if not c.is_generator_simple(x, mod):
#         continue
#     r = pow(x, order, mod)
#     g = set([c.G().pow_mod(x, y, mod) for y in range(mod)])
#     if r == 1:
#         print(x, g)

# , [pow(x, y, mod) for y in factors]
# for mod in range(1,20):
#     for g in range(2,mod):
#         if c.is_generator_simple(g, mod):
#             print(g, mod)


# for mod in range(20, 50):
#     generators = [y for y in range(mod) if len(set([test.pow_mod(y, x, mod) for x in range(mod)])) == mod - 1]
#     if len(generators) > 0:
#         print(c.factors(mod - 1))
#         print(mod, generators)

# dh = c.DiffieHellman()
# (x, gX) = dh.sample()
# print("x", x)
# print("gX", gX)
#
# (y, gY) = dh.sample()
# print("y", y)
# print("gY", gY)
#
# aliceKey = dh.key(gY, x)
# bobKey = dh.key(gX, y)
#
# print("alice", aliceKey)
# print("bob", bobKey)


alice_prime = misc.gen_prime(0, 330)
alice_generator = misc.gen_generator(alice_prime)

bob_prime = misc.gen_prime(330, 621)
bob_generator = misc.gen_generator(bob_prime)


Alice = cramer_shoup_encryption.CramerShoupEncryption.key_gen(alice_prime, alice_generator)
Bob = cramer_shoup_encryption.CramerShoupEncryption.key_gen(bob_prime, bob_generator)


m1 = 7983 % Bob.key_params.prime
m2 = 8880 % Bob.key_params.prime
print("m1: ", m1)
print("m2: ", m2)

C1 = cramer_shoup_encryption.CramerShoupEncryption.enc(Bob.public_key, Alice.key_params, m1)
C2 = cramer_shoup_encryption.CramerShoupEncryption.enc(Bob.public_key, Alice.key_params, m2)
#C3 = {}
#for key in C1:
#     C3[key] = c.cramer_shoup.mul_mod(Bob, C1[key], C2[key], Bob.p)

print("C1: ", C1)
print("C2: ", C2)
#print("C3: ", C3)

dec_m1 = cramer_shoup_encryption.CramerShoupEncryption.dec(Bob.secret_key, Bob.key_params, C1)
print("dec m1: ", dec_m1)
dec_m2 = cramer_shoup_encryption.CramerShoupEncryption.dec(Bob.secret_key, Bob.key_params, C2)
print("dec m2: ", dec_m2)

# print("homomorphism - Test")
# dec_m3 = Bob.dec(C3)

# print("dec m3: ", dec_m3)


p = misc.gen_prime(3, 621)
g = misc.gen_generator(p)

Bob = elgamal_encryption.ElGamalEncryption.key_gen(p, g)
Alice = elgamal_encryption.ElGamalEncryption.key_gen(p, g)

print("Bob keys: ", Bob.public_key, Bob.secret_key)
print("Alice Key: ", Alice.public_key, Alice.secret_key)

m = 32
print("Original Message", m)

mEnc = elgamal_encryption.ElGamalEncryption.enc(Alice.public_key, Bob.key_params, m)
print("Encrypted", mEnc.c1, mEnc.c2)

mDec = elgamal_encryption.ElGamalEncryption.dec(Alice.secret_key, Alice.key_params, mEnc)
print("Decrypted", mDec)

# ------------------------------- Threshhold El-Gamal -------------------------------------------
# playerCount = 3
# securityParameter = 100
#
#
# thElGamal = c.Threshhold_ElGamal(playerCount,securityParameter)
# pKey, sKeys = thElGamal.keyGen()
#
# print("Secret Keys: ", sKeys)
# print("Public Key: ", pKey)
#
# sKey = thElGamal.calcSecretKey(sKeys)
# print("Calculated Secret Key:", sKey)
#
# m = 2345
# print ("Original Message: ", m)
#
# mEnc = thElGamal.encrypt(pKey, m)
# print ("Encrypted Message: ", mEnc)
#
# mDec = thElGamal.decrypt(sKeys, mEnc)
# print ("Decrypted Message:", mDec)
#
#
#
# f = c.FDH_RSA()
# pk, sk = f.key_gen()
# m = "Hallo"
# sign = f.sign(sk, m)
# print("Verifikation:", f.verify(pk, m, sign))