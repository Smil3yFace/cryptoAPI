package cryptoapi.math_lib;

import cryptoapi.EGCDResult;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.*;

public class MathMisc {

    public static BigInteger randomBigInt(int size) {
        return new BigInteger(size, new SecureRandom());
    }

    public static BigInteger randomBigIntPrime(int secpar) {
        return BigInteger.probablePrime(secpar, new SecureRandom());
    }

    public static List<BigInteger> factorize(BigInteger x) {
        List<BigInteger> result = new ArrayList<>();
        BigInteger max_q = x.sqrt();
        BigInteger cur_q = BigInteger.valueOf(5);
        BigInteger step = BigInteger.valueOf(2);

        if (x.mod(BigInteger.TWO).equals(BigInteger.ZERO)) {
            cur_q = BigInteger.TWO;
        } else if (x.mod(BigInteger.valueOf(3)).equals(BigInteger.ZERO)) {
            cur_q = BigInteger.valueOf(3);
        } else {
            while (cur_q.compareTo(max_q) <= 0) {
                if (x.mod(cur_q).equals(BigInteger.ZERO)) {
                    break;
                }
                cur_q = cur_q.add(step);
                step = BigInteger.valueOf(6).subtract(step);
            }
        }

        if (cur_q.compareTo(max_q) <= 0) {
            result.add(cur_q);
            result.addAll(factorize(x.divide(cur_q)));
        } else {
            result.add(x);
        }

        return result;
    }

    public static HashMap<BigInteger, Integer> summariseFactors(List<BigInteger> primeFactors) {
        HashMap<BigInteger, Integer> factorCountMap = new HashMap<>();
        for (BigInteger factor : primeFactors) {
            factorCountMap.put(factor, factorCountMap.getOrDefault(factor, 0) + 1);
        }
        return factorCountMap;
    }

    public static BigInteger inverseEGCD(BigInteger a, BigInteger modulo) {
        return egcd(a,modulo).s.mod(modulo);
    }

    public static BigInteger inverseFermat(BigInteger a, BigInteger p) {
        BigInteger phi = p.subtract(BigInteger.ONE);
        return a.modPow(phi.subtract(BigInteger.ONE), p);
    }

    public static EGCDResult egcd(BigInteger a, BigInteger b) {
        if (a.equals(BigInteger.ZERO)) {
            return new EGCDResult(b, BigInteger.ZERO, BigInteger.ONE);
        } else {
            EGCDResult res = egcd(b.mod(a), a);
            BigInteger newX = res.t.subtract(b.divide(a).multiply(res.s));
            return new EGCDResult(res.gcd, newX, res.s);
        }
    }

    public static byte[] hash(BigInteger message) {
        return hash(message.toByteArray());
    }

    public static byte[] hash(byte[] message) {
        try {
            MessageDigest messageDigest = MessageDigest.getInstance("SHA3-512");
            return messageDigest.digest(message);
        } catch (NoSuchAlgorithmException ex) {
            //Should be thrown
            return null;
        }
    }

    public static BigInteger phi(HashMap<BigInteger, Integer> summarisedPrimeFactors) {
        BigInteger result = BigInteger.ONE;

        for (Map.Entry<BigInteger, Integer> entry : summarisedPrimeFactors.entrySet()) {
            BigInteger prime = entry.getKey();
            Integer exponent = entry.getValue();
            BigInteger primePower = prime.pow(exponent - 1);
            BigInteger primeMinusOne = prime.subtract(BigInteger.ONE);
            result = result.multiply(primePower.multiply(primeMinusOne));
        }

        return result;
    }

    public static BigInteger[] calcLagrangeCoeff(BigInteger[] xCoords) {
        // Initialize delta with BigInteger value of 1
        BigInteger[] delta = new BigInteger[xCoords.length];
        for (int i = 0; i < xCoords.length; i++) {
            delta[i] = BigInteger.ONE;
        }

        // Calculate Lagrange coefficients
        for (int i = 1; i < xCoords.length; i++) {
            for (int j = 1; j < xCoords.length; j++) {
                if (!xCoords[i].equals(xCoords[j])) {
                    BigInteger numerator = xCoords[0].subtract(xCoords[j]);
                    BigInteger denominator = xCoords[i].subtract(xCoords[j]);
                    delta[i] = delta[i].multiply(numerator.divide(denominator));
                }
            }
        }

        return delta;
    }
}
