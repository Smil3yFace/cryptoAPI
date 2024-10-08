package cryptoapi.cramer_shoup;

import java.math.BigInteger;

public class CramerShoupKeyParams {
    public final BigInteger prime;
    public final BigInteger generator;

    public CramerShoupKeyParams(BigInteger prime, BigInteger generator) {
        this.prime = prime;
        this.generator = generator;
    }

    public String toString() {
        String s = "{";
        s += "prime: " + this.prime;
        s += ", generator: " + this.generator;
        s += "}";
        return s;
    }
}

