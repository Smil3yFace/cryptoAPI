import cryptoapi.cramer_shoup.CramerShoupCipherText;
import cryptoapi.cramer_shoup.CramerShoupEncryption;
import cryptoapi.cramer_shoup.CramerShoupKeyPair;
import cryptoapi.diffie_hellman.*;
import cryptoapi.elgamal.*;
import cryptoapi.math_lib.MathMisc;
import cryptoapi.rsa.*;
import java.math.BigInteger;

public class Main {

	public static void main(String[] args) {
        diffieHellman();
        separateOutput();
        elGamal();
        separateOutput();
        fdhRsa();
        separateOutput();
        cramerShoup();
        separateOutput();
        fdhRsaAttack();
        separateOutput();
	}

    public static void fdhRsaAttack() {
        System.out.println("Start FDH RSA-Attack example...");

        // Paramaters
        int secpar = 32;
        BigInteger m1 = BigInteger.valueOf(131);
        BigInteger m2 = BigInteger.valueOf(89);

        RSAKeyPair keys = FulldomainHashRSAEncryption.keyGen(secpar);
        BigInteger sigma1 = FulldomainHashRSAEncryption.sign(keys.secretKey, m1);
        BigInteger sigma2 = FulldomainHashRSAEncryption.sign(keys.secretKey, m2);
        BigInteger sig_s = sigma2.multiply(sigma1);
        BigInteger m_s = m2.multiply(m1);

        System.out.println(FulldomainHashRSAEncryption.verify(keys.publicKey, m_s, sig_s));
    }

    public static void fdhRsa() {
        System.out.println("Start FDH RSA signing example...");

        // Paramaters
        int secpar = 32;
        BigInteger m = BigInteger.valueOf(131);

        RSAKeyPair keys = FulldomainHashRSAEncryption.keyGen(secpar);
        BigInteger sigma = FulldomainHashRSAEncryption.sign(keys.secretKey, m);

        System.out.println("Key pair: " + keys);
        System.out.println(FulldomainHashRSAEncryption.verify(keys.publicKey, m, sigma));
    }

    public static void elGamal() {
        System.out.println("Start ElGamal example...");
        // Define Security Parameter
        final int secpar = 32;

        // Bob
        ElGamalKeyPair bob = ElGamalEncryption.keyGen(secpar);
        System.out.println("Bob: " + bob);

        // Alice
        BigInteger m = new BigInteger("131");
        ElGamalCipherText ciphertext = ElGamalEncryption.enc(bob.publicKey, bob.keyParams, m);

        System.out.println("c1: " + ciphertext.c1);
        System.out.println("c2: " + ciphertext.c2);

        // Bob
        BigInteger mprime = ElGamalEncryption.dec(bob, ciphertext);

        compare(mprime, m);
    }

    public static void diffieHellman() {
        System.out.println("Start Diffie-Hellman key exchange example...");

        // Public Parameters
        final int secpar = 32;
        BigInteger p = MathMisc.randomBigIntPrime(secpar);
        BigInteger g = MathMisc.randomBigInt(secpar);
        System.out.println("prime: " + p);
        System.out.println("generator: " + g + "\n");

        // Alice
        DiffieHellmanKeyExchange alice = new DiffieHellmanKeyExchange(p,g);

        // Bob
        DiffieHellmanKeyExchange bob = new DiffieHellmanKeyExchange(p,g);

        // Alice shared key
        alice.generateShareKey(bob.publicKey);
        System.out.println("Alice: " + alice);

        //Bob shared key
        bob.generateShareKey(alice.publicKey);
        System.out.println("Bob: " + bob);

        compare(alice.getSharedKey(), bob.getSharedKey());
    }

    public static void cramerShoup() {
        System.out.println("Start Cramer-Shoup exchange example...");
        // Define Security Parameter
        final int secpar = 32;

        // Bob
        CramerShoupKeyPair bob = CramerShoupEncryption.keyGen(secpar);
        System.out.println("Bob: " + bob);

        // Alice
        BigInteger m = new BigInteger("131");
        CramerShoupCipherText ciphertext = CramerShoupEncryption.enc(bob.publicKey, bob.keyParams, m);

        System.out.println("cipherText: " + ciphertext);

        // Bob
        BigInteger mprime = CramerShoupEncryption.dec(bob.secretKey, bob.keyParams, ciphertext);

        compare(mprime, m);
    }

    private static<T> void compare(T firstValue, T secondValue) {
        if (firstValue.equals(secondValue)) {
            System.out.println(firstValue + " is equals to " + secondValue);
        } else {
            System.out.println("ERROR");
            System.out.println( firstValue + " doesn't match " + secondValue);
        }
    }

    private static void separateOutput() {
        System.out.println();
        System.out.println();
    }
}
