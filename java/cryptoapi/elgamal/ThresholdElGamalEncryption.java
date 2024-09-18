package cryptoapi.elgamal;

import cryptoapi.math_lib.CyclicMultiplicativeGroup;
import cryptoapi.math_lib.MathMisc;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.stream.Stream;

public class ThresholdElGamalEncryption {

    public static ThresholdElGamalKeyCollection keyGen(int secPar, int numOfPlayers) {
        CyclicMultiplicativeGroup group = new CyclicMultiplicativeGroup(MathMisc.randomBigIntPrime(secPar));
        BigInteger generator = group.getGenerator();
        int polynomDegree = numOfPlayers - 1;

        BigInteger[] xCoordsOfPlayers = new BigInteger[numOfPlayers + 1];
        BigInteger[] delta = MathMisc.calcLagrangeCoeff(xCoordsOfPlayers);
        BigInteger[] yCoordsOfPlayers = new BigInteger[numOfPlayers];

        // Generate random y-coordinates for players
        for (int i = 0; i < numOfPlayers; i++) {
            yCoordsOfPlayers[i] = group.randomElement();
        }

        // Initialize secret keys
        BigInteger[] secretKeys = new BigInteger[numOfPlayers + 1];
        for (int n = 1; n < xCoordsOfPlayers.length; n++) {
            secretKeys[n] = BigInteger.ZERO;
            for (int p = 0; p < numOfPlayers; p++) {
                secretKeys[n] = secretKeys[n].add(yCoordsOfPlayers[p].multiply(xCoordsOfPlayers[n].pow(p)));
            }
        }

        secretKeys[0] = calcSharedSecret(secretKeys, delta);
        BigInteger publicKey = group.powMod(generator, secretKeys[0]);
        secretKeys[0] = BigInteger.ZERO; // Reset the shared secret key

        return new ThresholdElGamalKeyCollection(
                new ElGamalKeyParams(group.m, generator),
                publicKey,
                Arrays.stream(secretKeys, 1, secretKeys.length).toArray(BigInteger[]::new),
                delta
        );
    }

    public static ElGamalCipherText enc(BigInteger otherPublicKey, ElGamalKeyParams keyParams, BigInteger message) {
        return ElGamalEncryption.enc(otherPublicKey, keyParams, message);
    }

    public static BigInteger dec(ThresholdElGamalKeyCollection keyCollection, ElGamalCipherText ciphertext) {
        BigInteger sharedSecret = calcSharedSecret(keyCollection.individualSecretKeys, keyCollection.delta);

        return ElGamalEncryption.dec(
            new ElGamalKeyPair(
                keyCollection.keyParams,
                sharedSecret,
                keyCollection.publicKey
            ),
            ciphertext
        );
    }

    private static BigInteger calcSharedSecret(BigInteger[] secretKeys, BigInteger[] delta) {
        BigInteger sharedSecret = BigInteger.ZERO;
        for (int i = 1; i < delta.length; i++) {
            sharedSecret = sharedSecret.add(delta[i].multiply(secretKeys[i]));
        }
        return sharedSecret;
    }
}

