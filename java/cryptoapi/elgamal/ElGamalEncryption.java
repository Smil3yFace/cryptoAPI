package cryptoapi.elgamal;

import cryptoapi.math_lib.CyclicMultiplicativeGroup;
import cryptoapi.math_lib.MathMisc;

import java.math.BigInteger;

public class ElGamalEncryption {

    public static ElGamalKeyPair keyGen(int secPar) {
        CyclicMultiplicativeGroup group = new CyclicMultiplicativeGroup(MathMisc.randomBigIntPrime(secPar));

        ElGamalKeyParams publicParams = new ElGamalKeyParams(group.randomElement(), group.m);
        BigInteger secretKey = group.randomElement();
        BigInteger publicKey = group.powMod(publicParams.generator, secretKey);

        return new ElGamalKeyPair(publicParams, secretKey, publicKey);
    }

    public static ElGamalCipherText enc(BigInteger otherPublicKey, ElGamalKeyParams keyParams, BigInteger message) {
        CyclicMultiplicativeGroup group = new CyclicMultiplicativeGroup(keyParams.prime);

        BigInteger y = group.randomElement();
        BigInteger c1 = group.powMod(keyParams.generator, y);

        BigInteger c2Prime = group.powMod(otherPublicKey, y);
        BigInteger c2 = group.mulMod(c2Prime, message);

        return new ElGamalCipherText(c1, c2);
    }

    public static BigInteger dec(ElGamalKeyPair keypair, ElGamalCipherText cipherText) {
        CyclicMultiplicativeGroup group = new CyclicMultiplicativeGroup(keypair.keyParams.prime);

        // Reconstructing Shared key
        BigInteger k = group.powMod(cipherText.c1, keypair.secretKey);
        BigInteger kinv = group.mulInvertMod(k);

        return group.mulMod(cipherText.c2, kinv);
    }
}
