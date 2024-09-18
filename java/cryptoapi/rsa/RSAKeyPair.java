package cryptoapi.rsa;

import java.math.BigInteger;

public class RSAKeyPair {

    public final RSAKeyTuple publicKey;

    public final RSAKeyTuple secretKey;

    public RSAKeyPair(BigInteger publicKey, BigInteger secretKey, BigInteger modul) {
        this.publicKey = new RSAKeyTuple(publicKey, modul);
        this.secretKey = new RSAKeyTuple(secretKey, modul);
    }

    public String toString() {
        String s = "{";
        s += "publicKey: " + this.publicKey;
        s += ", secretKey: " + this.secretKey;
        s += "}";
        return s;
    }
}
