package cryptoapi.elgamal;

import java.math.BigInteger;

public class ElGamalCipherText {
    public final BigInteger c1;
    public final BigInteger c2;

    public ElGamalCipherText(BigInteger c1, BigInteger c2) {
        this.c1 = c1;
        this.c2 = c2;
    }

    public String toString() {
        String s = "{";
        s += "c1: " + this.c1;
        s += ", c2: " + this.c2;
        s += "}";
        return s;
    }
}
