from PIL import Image
import numpy as np
import math
from ecdsa import ellipticcurve, SECP256k1, numbertheory
import os


def imageLoader(image_path):
    image = Image.open(image_path)
    pixels = np.array(image, dtype=object)
    num_channels = pixels.shape[2]
    encrypted_pixels = pixels + np.random.randint(1, 2)
    return encrypted_pixels, num_channels, image.size


def pixelsGrouping(encrypted_pixels):
    flat_pixels = encrypted_pixels.flatten()
    pixelPerGroup = len(getPixelsFromGroup(len(flat_pixels), 258)) - 1
    groupsNumber = math.ceil(len(flat_pixels) / pixelPerGroup)
    large_integers = [
        makeGroupFromPixels(flat_pixels[i : i + pixelPerGroup], 258)
        for i in range(0, groupsNumber, pixelPerGroup)
    ]
    return large_integers


def makeGroupFromPixels(pixels, base):
    num = 0
    for pixel in pixels:
        num = num * base + pixel
    return num


def getPixelsFromGroup(n, base):
    if n == 0:
        digits = [0]
    else:
        digits = []
        while n:
            n, remainder = divmod(n, base)
            digits.append(remainder)
        digits.reverse()
    return digits


def ECC_Operator(large_integers, k, Pb):
    kG = k * SECP256k1.generator
    kPb = k * Pb.pubkey.point
    Pc = [kPb + pointFromPixel(i) for i in large_integers]
    return Pc, kG


def pointFromPixel(pixel):
    x = pixel
    y = (x**3 + SECP256k1.curve.a() * x + SECP256k1.curve.b()) % SECP256k1.curve.p()
    return ellipticcurve.PointJacobi(SECP256k1.curve, x, y, 0)


def bytesConvertor(cipher_text):
    byte_array = list()
    for item in cipher_text:
        pixel = pixelfromPoint(item)
        pixels = getPixelsFromGroup(pixel, 258)
        print(len(pixels))
        byte_array.extend(pixels)
    return byte_array


def pixelfromPoint(point):
    return point.x()


def imageBuilder(cipher_bytes, width, height, num_channels):
    expected_size = width * height * num_channels
    adjusted_cipher_bytes = np.array(cipher_bytes[:expected_size]).reshape(
        (height, width, num_channels)
    )
    reconstructed_image = Image.fromarray(adjusted_cipher_bytes.astype("uint8"))
    reconstructed_image.save("encrypted_image.png")


def imageEncryptor(image_path, public_key):
    encrypted_pixels, num_channels, (width, height) = imageLoader(image_path)
    large_integers = pixelsGrouping(encrypted_pixels)
    cipher_text, generator = ECC_Operator(
        large_integers,
        int.from_bytes(os.urandom(32), "big") % SECP256k1.order,
        public_key,
    )
    cipher_bytes = bytesConvertor(cipher_text)
    imageBuilder(
        cipher_bytes, width, height, math.ceil(len(cipher_bytes) / (width * height))
    )
    print("Image encryption and reconstruction complete.")
    return generator
