from PIL import Image
import numpy as np

def imageLoader(image_path):
    image = Image.open(image_path)
    pixels = np.array(image, dtype=np.int64)
    height, width, num_channels = pixels.shape
    return pixels, height, width, num_channels

def pixelsFlatter(pixels):
    flat_pixels = pixels.flatten()
    return [(flat_pixels[i], flat_pixels[i+1]) for i in range(0, len(flat_pixels) - 1, 2)]

def decryptor(paired_values, private_key):
    decrypted_values = []
    for a, b in paired_values:
        kG = (a * private_key) % 256
        nB = (b * private_key) % 256
        value = (a + b - (kG - nB)) % 256
        normalized_value = (value - 2) % 256
        decrypted_values.append(normalized_value)
    return decrypted_values

def imageBuilder(decrypted_values, width, height, num_channels, output_path):
    if len(decrypted_values) < width * height * num_channels:
        decrypted_values += [0] * (width * height * num_channels - len(decrypted_values))
    else:
        decrypted_values = decrypted_values[:width * height * num_channels]
    
    decrypted_array = np.array(decrypted_values).reshape(height, width, num_channels).astype('uint8')
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Decryption complete. Image saved as {output_path}")

def imageDecryptor(cipher_image_path, private_key, output_image_path='decrypted_image.png'):
    pixels, height, width, num_channels = imageLoader(cipher_image_path)
    paired_values = pixelsFlatter(pixels)
    decrypted_values = decryptor(paired_values, private_key)
    imageBuilder(decrypted_values, width, height, num_channels, output_image_path)
