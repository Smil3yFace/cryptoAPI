package cryptoapi.elgamal;

import java.math.BigInteger;

public class ElGamalKeyPair {
    public final ElGamalKeyParams keyParams;
    public final BigInteger publicKey;
    public final BigInteger secretKey;

    protected ElGamalKeyPair(ElGamalKeyParams keyParams, BigInteger secretKey, BigInteger publicKey) {
        this.secretKey = secretKey;
        this.publicKey = publicKey;
        this.keyParams = keyParams;
    }

    @Override
    public String toString() {
        String s = "{";
        s += "publicParams: " + this.keyParams.toString();
        s += ", publicKey: " + this.publicKey;
        s += ", secretKey: " + this.secretKey;
        s += "}";
        return s;
    }
}
