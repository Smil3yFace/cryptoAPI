package cryptoapi.cramer_shoup;

import java.math.BigInteger;

public class CramerShoupCipherText {
    public final BigInteger R;
    public final BigInteger R_;
    public final BigInteger P;
    public final BigInteger T;

    public CramerShoupCipherText(BigInteger R, BigInteger R_, BigInteger P, BigInteger T) {
        this.R = R;
        this.R_ = R_;
        this.P = P;
        this.T = T;
    }

    public String toString() {
        String s = "{";
        s += "R: " + this.R;
        s += ", R_: " + this.R_;
        s += ", P: " + this.P;
        s += ", T: " + this.T;
        s += "}";
        return s;
    }
}