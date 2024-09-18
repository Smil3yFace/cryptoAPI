package cryptoapi.rsa;

import cryptoapi.math_lib.MathMisc;

import java.math.BigInteger;

public class FulldomainHashRSAEncryption extends RSAEncryption {


    public static BigInteger sign(RSAKeyTuple keyTuple, BigInteger m) {
        return new BigInteger(MathMisc.hash(m)).modPow(keyTuple.key, keyTuple.modul);
    }

    public static boolean verify(RSAKeyTuple publicKey, BigInteger m, BigInteger sigma) {
        BigInteger h = new BigInteger(MathMisc.hash(m));
        return h.mod(publicKey.modul).equals(sigma.modPow(publicKey.key, publicKey.modul));
    }
}
