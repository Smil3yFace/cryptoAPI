package cryptoapi.cramer_shoup;

import java.math.BigInteger;

public class CramerShoupPublicKey {
    public final BigInteger A;
    public final BigInteger B;
    public final BigInteger B_;
    public final BigInteger generator;
    public final BigInteger g_;
    public final BigInteger prime;

    public CramerShoupPublicKey(BigInteger A, BigInteger B, BigInteger B_, BigInteger generator, BigInteger g_, BigInteger prime) {
        this.A = A;
        this.B = B;
        this.B_ = B_;
        this.generator = generator;
        this.g_ = g_;
        this.prime = prime;
    }
}
