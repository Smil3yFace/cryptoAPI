package cryptoapi.math_lib;

import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.Random;

public class CyclicMultiplicativeGroup extends MultiplicativeGroup {

    public CyclicMultiplicativeGroup(BigInteger modulo) {
        super(modulo);
    }

    public BigInteger getGenerator() {
        BigInteger g = null;
        if (!this.m.isProbablePrime(100)) {
            return g;
        } else {
            BigInteger r = new BigInteger(m.bitLength(), new SecureRandom()).mod(m.divide(BigInteger.valueOf(4L)));
            boolean found = false;

            while(!found) {
                g = BigInteger.TWO.multiply(r).add(BigInteger.ONE);
                found = g.compareTo(m) < 0 && g.isProbablePrime(100);
            }
            return g;
        }
    }
}
