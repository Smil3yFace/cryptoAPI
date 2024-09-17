package cryptoapi.cramer_shoup;

public class CramerShoupKeyPair {
    public final CramerShoupSecretKey secretKey;
    public final CramerShoupPublicKey publicKey;
    public final CramerShoupKeyParams keyParams;

    public CramerShoupKeyPair(CramerShoupSecretKey secretKey, CramerShoupPublicKey publicKey, CramerShoupKeyParams keyParams) {
        this.secretKey = secretKey;
        this.publicKey = publicKey;
        this.keyParams = keyParams;
    }
}
