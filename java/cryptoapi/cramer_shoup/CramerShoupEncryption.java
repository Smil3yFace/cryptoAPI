package cryptoapi.cramer_shoup;

import cryptoapi.math_lib.CyclicMultiplicativeGroup;
import cryptoapi.math_lib.MathMisc;

import java.math.BigInteger;
import java.security.SecureRandom;

public class CramerShoupEncryption {

    public static CramerShoupKeyPair keyGen(int secParam) {
        CyclicMultiplicativeGroup group = new CyclicMultiplicativeGroup(MathMisc.randomBigIntPrime(secParam));
        CramerShoupKeyParams keyParams = new CramerShoupKeyParams(group.m, group.getGenerator());

        CramerShoupSecretKey secretKey = new CramerShoupSecretKey(
                // alpha
                group.randomElement(),
                // x
                group.randomElement(),
                // y
                group.randomElement(),
                // z
                group.randomElement(),
                // z_
                group.randomElement(),
                // w
                group.randomElement(),
                // w_
                group.randomElement()
        );

        BigInteger g_ = group.powMod(keyParams.generator, secretKey.alpha);
        CramerShoupPublicKey publicKey = new CramerShoupPublicKey(
                // A
                group.mulMod(
                        group.powMod(keyParams.generator, secretKey.x),
                        group.powMod(g_, secretKey.y)
                ),
                // B
                group.mulMod(
                        group.powMod(keyParams.generator, secretKey.z),
                        group.powMod(g_, secretKey.w)
                ),
                // B_
                group.mulMod(
                        group.powMod(keyParams.generator, secretKey.z_),
                        group.powMod(g_, secretKey.w_)
                ),
                keyParams.generator,
                g_,
                keyParams.prime
        );

        return new CramerShoupKeyPair(secretKey, publicKey, keyParams);
    }

    public CramerShoupCipherText enc(CramerShoupPublicKey otherPublicKey, CramerShoupKeyParams keyParams, BigInteger message) {
        CyclicMultiplicativeGroup group = new CyclicMultiplicativeGroup(otherPublicKey.prime);

        BigInteger r = new BigInteger(keyParams.prime.bitLength(), new SecureRandom()).mod(keyParams.prime.subtract(BigInteger.ONE));

        BigInteger R = group.powMod(otherPublicKey.generator, r);
        BigInteger R_ = group.powMod(otherPublicKey.g_, r);
        BigInteger A_r = group.powMod(otherPublicKey.A, r);
        BigInteger P = group.mulMod(A_r, message);

        String beta = R_.toString() + R.toString() + P.toString();
        BigInteger h = new BigInteger(1, MathMisc.hash(beta.getBytes())).mod(group.order);

        BigInteger B_h = group.powMod(otherPublicKey.B_, h);
        BigInteger B_B_h = group.mulMod(otherPublicKey.B, B_h);
        BigInteger T = group.powMod(B_B_h, r);

        return new CramerShoupCipherText(R, R_, P, T);
    }

    public static BigInteger dec(CramerShoupSecretKey secretKey, CramerShoupKeyParams keyParams, CramerShoupCipherText ciphertext) {

        CyclicMultiplicativeGroup group = new CyclicMultiplicativeGroup(keyParams.prime);

        String beta = ciphertext.R_.toString() + ciphertext.R.toString() + ciphertext.P.toString();
        BigInteger h = new BigInteger(1, MathMisc.hash(beta.getBytes())).mod(group.order);

        BigInteger T_Val1 = group.mulMod(
                group.powMod(ciphertext.R, secretKey.z),
                group.powMod(ciphertext.R, h.multiply(secretKey.z_).mod(group.order))
        );

        BigInteger T_Val2 = group.mulMod(
                group.powMod(ciphertext.R_, secretKey.w),
                group.powMod(ciphertext.R_, h.multiply(secretKey.w_).mod(group.order))
        );

        if (ciphertext.T.equals(group.mulMod(T_Val1, T_Val2))) {
            BigInteger Rx = group.powMod(ciphertext.R, secretKey.x);
            BigInteger R_y = group.powMod(ciphertext.R_, secretKey.y);
            BigInteger inverse_RxR_y = group.mulInvertMod(Rx.multiply(R_y));

            return group.mulMod(ciphertext.P, inverse_RxR_y);
        } else {
            throw new RuntimeException("Validation error");
        }
    }
}
