from math import floor, sqrt
import random
import hashlib
from typing import Tuple
'''
    def sample(self):
        x = random.randint(0, self.p - 1)
        bigX = self.pow_mod(self.g, x, self.p)
        return x, bigX
'''

class ElGamal(DiffieHellman):
    def enc(self, pub, m):
        (y, gY) = self.sample()
        c2 = self.mul_mod(self.key(pub, y), m, self.p)
        c1 = gY
        return c1, c2

    def dec(self, sec, c):
        c1, c2 = c
        sharedKey = self.key(c1, sec)
        sharedKeyInv = self.mul_invert_mod(sharedKey, self.p)
        return self.mul_mod(c2, sharedKeyInv, self.p)

    def keyGen(self):
        return self.sample()

class Threshhold_ElGamal(ElGamal):
    def __init__(self, players, secPar):
        self.players = players
        self.degree = players - 1
        self.secPar = secPar
        self.xCoords = [x for x in range(0, self.players + 1)]
        self.delta = self.lagrangeCoeff()

    # Coords for Players start at 1 and increase by 1 each
    # Coords for x0 is 0
    def lagrangeCoeff(self):
        delta = [1 for x in range(0, self.players + 1)]
        for i in range(1, self.players + 1):
            for j in range(1, self.players + 1):
                if i != j:
                    delta[i] *= (self.xCoords[0] - self.xCoords[j]) / (self.xCoords[i] - self.xCoords[j])
        return delta

    # Summe von 1 bis players + 1 von delta * y 
    def calcSecretKey(self, sKey):
        sKey[0] = 0
        for i in range (1, self.players + 1):
            sKey[0] += self.delta[i] * sKey[i]
        return int(sKey[0])

    def keyGen(self):
        pA = [random.randint(0, self.secPar) for x in range(0,self.players)]

        pX = [0 for x in range(0, self.players + 1)]
        for n in range(1, self.players + 1):
            for i in range(0, self.players):
                pX[n] += pA[i] * (self.xCoords[n] ^ i)

        pX[0] = self.calcSecretKey(pX)
        pKey = self.pow_mod(self.g, pX[0], self.p)
        pX[0] = 0
        sKey = pX
        
        return pKey, sKey

    def encrypt(self, pKey, m):
        return self.enc(pKey, m)

    def decrypt(self, sKeys, c):
        return self.dec(self.calcSecretKey(sKeys), c)

    # "CipherText Share" als Funktion
    # Input: c1 vom Chiffrat und Share von Player p[i]
    # Output: c1 hoch Share


    # "Threshhold Decrypt" Funktion
    # Input: Output von Ciphertext Share von allen Players
    # Rekonstruiert den Secret Key im Exponent


class FDH_RSA(G):
    def __init__(self):
        self.hash = hashlib.sha3_512
        self.p = genPrime(1000, 2000)
        self.q = genPrime(1000, 2000)
        self.n = self.p * self.q
        self.phi = self.order(self.n)

    @staticmethod
    def egcd(a: int, b: int) -> Tuple[int, int, int]:
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = FDH_RSA.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def key_gen(self):
        e = random.randint(0, self.phi)
        while FDH_RSA.egcd(e, self.phi)[0] != 1:
            e = random.randint(0, self.phi)

        # self.mul_invert_mod(e, self.phi)
        d = pow(e, -1, self.phi)

        pk = (e, self.n)
        sk = (d, self.n)

        return pk, sk

    def sign(self, sk: Tuple[int, int], m: str):
        h = int(self.hash(m.encode()).hexdigest(), 16)
        return pow(h, sk[0], sk[1])

    def verify(self, pk: Tuple[int, int], m: str, sigma: int):
        h = int(self.hash(m.encode()).hexdigest(), 16)
        return h % self.n == pow(sigma, pk[0], pk[1])