package cryptoapi.diffie_hellman;

import cryptoapi.math_lib.CyclicMultiplicativeGroup;
import cryptoapi.math_lib.MathMisc;
import java.math.BigInteger;

public class DiffieHellmanKeyExchange {
    public final BigInteger publicKey;
    public final BigInteger secretKey;
    private BigInteger sharedKey = null;

    private final CyclicMultiplicativeGroup group;

    public DiffieHellmanKeyExchange(BigInteger prime, BigInteger generator) {
        this.group = new CyclicMultiplicativeGroup(prime);
        this.secretKey = this.group.randomElement();
        this.publicKey = this.group.powMod(generator, secretKey);
    }

    public void generateShareKey(BigInteger otherPublicKey) {
        this.sharedKey = this.group.powMod(otherPublicKey, this.secretKey);
    }

    public BigInteger getSharedKey() {
        return this.sharedKey;
    }

    @Override
    public String toString() {
        String s = "{";
        s += "sharedKey: " + this.sharedKey;
        s += ", publicKey: " + this.publicKey;
        s += ", secretKey: " + this.secretKey;
        s += "}";
        return s;
    }
}
