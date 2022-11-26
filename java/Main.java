import cryptoapi.EGCDResult;
import cryptoapi.MathLib;
import cryptoapi.diffiehellman.*;
import cryptoapi.elgamal.*;
import cryptoapi.rsa.*;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) {
        //diffieHellman();
        //elGamal();
        rsa();
	}

    public static void rsa_attack_example() {
        System.out.println("Start RSA-Attack example...");

        // Paramaters
        int secpar = 16;
        BigInteger m1 = BigInteger.valueOf(15);
        BigInteger m2 = BigInteger.valueOf(32);

        RSAKeyPair keys = RSAEncryption.keyGen(secpar);
        BigInteger sigma1 = RSAEncryption.sign(keys, m1);
        BigInteger sigma2 = RSAEncryption.sign(keys, m2);
        BigInteger sig_s = sigma2.multiply(sigma1);
        BigInteger m_s = m2.multiply(m1);

        System.out.println(RSAEncryption.verify(keys.publicKey,m_s, sig_s));
    }

    public static void rsa() {
        System.out.println("Start RSA signing example...");

        // Paramaters
        int secpar = 16;
        BigInteger m = BigInteger.valueOf(15);

        RSAKeyPair keys = RSAEncryption.keyGen(secpar);
        BigInteger sigma = RSAEncryption.sign(keys, m);

        System.out.println("Key pair: " + keys);
        System.out.println(RSAEncryption.verify(keys.publicKey, m, sigma));
    }

    public static void elGamal() {
        System.out.println("Start ElGamal example...");
        // Define Security Parameter
        final int secpar = 128;

        // Bob
        ElGamalKeyPair bob = ElGamalEncryption.keyGen(secpar);
        System.out.println("Bob: " + bob);

        // Alice
        BigInteger m = new BigInteger("100000");
        BigInteger[] ciphretexts = ElGamalEncryption.enc(bob.publicKey, bob.keyParams, m);
        BigInteger c1 = ciphretexts[0];
        BigInteger c2 = ciphretexts[1];

        System.out.println("c1: " + c1);
        System.out.println("c2: " + c2);

        // Bob
        BigInteger mprime = ElGamalEncryption.dec(bob, c1, c2);

        compare(mprime, m);

        //Separation to the following output
        System.out.println();
        System.out.println();
    }

    public static void diffieHellman() {
        System.out.println("Start Diffie-Hellman key exchange example...");

        // Public Parameters
        final int securityParam = 64;
        BigInteger p = MathLib.randomPrime(securityParam);
        BigInteger g = MathLib.random(p);
        System.out.println("prime: " + p);
        System.out.println("generator: " + g + "\n");

        // Alice
        DiffieHellmanKeyExchange alice = new DiffieHellmanKeyExchange(p,g);

        // Bob
        DiffieHellmanKeyExchange bob = new DiffieHellmanKeyExchange(p,g);

        // Alice shared key
        alice.generateShareKey(bob.getPublicKey());
        System.out.println("Alice: " + alice);

        //Bob shared key
        bob.generateShareKey(alice.getPublicKey());
        System.out.println("Bob: " + bob);

        compare(alice.getSharedKey(), bob.getSharedKey());

        //Separation to the following output
        System.out.println();
        System.out.println();

    }

    static<T> void compare(T firstValue, T secondValue) {
        if (firstValue.equals(secondValue)) {
            System.out.println(firstValue + " is equals to " + secondValue);
        } else {
            System.out.println("ERROR");
            System.out.println( firstValue + " doesn't match " + secondValue);
        }
    }
}
