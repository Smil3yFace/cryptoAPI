package cryptoapi.elgamal;

import java.math.BigInteger;
import java.util.List;
import java.util.stream.Stream;

public class ThresholdElGamalKeyCollection {
    public final ElGamalKeyParams keyParams;
    public final BigInteger publicKey;
    public final BigInteger[] individualSecretKeys;
    public final BigInteger[] delta;

    public ThresholdElGamalKeyCollection(ElGamalKeyParams keyParams, BigInteger publicKey, BigInteger[] individualSecretKeys, BigInteger[] delta) {
        this.keyParams = keyParams;
        this.publicKey = publicKey;
        this.individualSecretKeys = individualSecretKeys;
        this.delta = delta;
    }

    public List<ElGamalKeyPair> getElGamalKeyPairs() {
        return Stream.of(individualSecretKeys)
            .map(sk -> new ElGamalKeyPair(keyParams, sk, publicKey))
            .toList();
    }
}
