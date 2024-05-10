from imageEncryptor import imageEncryptor
from imageDecryptor import imageDecryptor
from ecdsa import SigningKey, SECP256k1


def generate_keys():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key


def main():
    receiverPrivateKey, receiverPublicKey = generate_keys()
    generator = imageEncryptor("Assets/Resources/Cat.jpg", receiverPublicKey)
    # imageDecryptor("encrypted_image.png", private_key=receiverPrivateKey)


if __name__ == "__main__":
    main()
