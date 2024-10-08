package cryptoapi.cramer_shoup;

import java.math.BigInteger;

public class CramerShoupSecretKey {
    public final BigInteger alpha;
    public final BigInteger x;
    public final BigInteger y;
    public final BigInteger z;
    public final BigInteger z_;
    public final BigInteger w;
    public final BigInteger w_;

    public CramerShoupSecretKey(BigInteger alpha, BigInteger x, BigInteger y, BigInteger z, BigInteger z_, BigInteger w, BigInteger w_) {
        this.alpha = alpha;
        this.x = x;
        this.y = y;
        this.z = z;
        this.z_ = z_;
        this.w = w;
        this.w_ = w_;
    }

    public String toString() {
        String s = "{";
        s += "x: " + this.x;
        s += ", y: " + this.y;
        s += ", z: " + this.z;
        s += ", z_: " + this.z_;
        s += ", w: " + this.w;
        s += ", w_: " + this.w_;
        s += "}";
        return s;
    }
}

