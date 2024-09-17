package cryptoapi.math_lib;

import java.math.BigInteger;

public class AdditiveGroup {
    public final BigInteger modulo;
    public final BigInteger order;

    public AdditiveGroup(BigInteger modulo) {
        this.modulo = modulo;
        this.order = modulo;
    }

    public BigInteger addMod(BigInteger x, BigInteger y) {
        return x.add(y).mod(this.modulo);
    }

    public BigInteger subMod(BigInteger x, BigInteger y) {
        return addMod(x, additiveInverse(y));
    }

    public BigInteger additiveInverse(BigInteger x) {
        return x.negate().add(this.modulo).mod(this.modulo);
    }

    public BigInteger powMod(BigInteger base, BigInteger power) {
        BigInteger result = BigInteger.ZERO;
        for (BigInteger i = BigInteger.ZERO; i.compareTo(power) < 0; i = i.add(BigInteger.ONE)) {
            result = addMod(result, base);
        }
        return result;
    }
}
