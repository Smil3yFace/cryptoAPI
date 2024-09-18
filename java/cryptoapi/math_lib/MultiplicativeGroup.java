package cryptoapi.math_lib;

import java.math.BigInteger;
import java.security.SecureRandom;

public class MultiplicativeGroup {
    public final BigInteger m;
    public final BigInteger order;
    private final SecureRandom random = new SecureRandom();

    public MultiplicativeGroup(BigInteger modulo) {
        this.m = modulo;
        this.order = MathMisc.phi(MathMisc.summariseFactors(MathMisc.factorize(modulo)));
    }

    public BigInteger mulMod(BigInteger x, BigInteger y) {
        return x.multiply(y).mod(m);
    }

    public BigInteger powMod(BigInteger base, BigInteger power) {
        return base.modPow(power, this.m);
    }

    public BigInteger mulInvertMod(BigInteger x) {
        return x.modPow(order.subtract(BigInteger.ONE), m);
    }

    public BigInteger wrapping(BigInteger x) {
        return x.mod(m).add(m).mod(m);
    }

    public BigInteger randomElement() {
        return new BigInteger(m.bitLength(), random).mod(m);
    }
}
