package cryptoapi.rsa;

import cryptoapi.math_lib.MathMisc;

import java.math.BigInteger;

public class RSAEncryption{

    public static RSAKeyPair keyGen(int secpar) {
        // Paramaters
        BigInteger p = MathMisc.randomBigIntPrime(secpar);
        BigInteger q = MathMisc.randomBigIntPrime(secpar);
        BigInteger N = p.multiply(q);
        BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE)).mod(N);

        BigInteger e = sampleE(phi);
        BigInteger d = e.modPow(BigInteger.ONE.negate(), phi);

        // sk = e, N
        // pk = d, N
        return new RSAKeyPair(d, e, N);
    }

    public static BigInteger enc(RSAKeyTuple otherPublicKey, BigInteger message) {
        return message.modPow(otherPublicKey.key, otherPublicKey.modul);
    }

    public static BigInteger dec(RSAKeyTuple privateKey, BigInteger ciphertext) {
        return ciphertext.modPow(privateKey.key, privateKey.modul);
    }

    public static BigInteger sampleE(BigInteger phi) {
        BigInteger e;
        do {
            e = MathMisc.randomBigInt(phi.bitLength()).mod(phi);
        } while (!e.gcd(phi).equals(BigInteger.ONE) && !e.equals(BigInteger.ONE));
        return e;
    }
}
