from PIL import Image
import numpy as np
import random

# Step 1: Load the image and encrypt by modifying pixel values
def load_and_encrypt_image(image_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    num_channels = pixels.shape[2] if len(pixels.shape) > 2 else 1
    encrypted_pixels = pixels + np.random.randint(1, 10000, size=pixels.shape)
    return encrypted_pixels, num_channels, image.size

# Step 2 & 3: Group pixels and convert to integers, then prepare the plain message
def pixels_to_large_integers(encrypted_pixels):
    flat_pixels = encrypted_pixels.flatten()
    large_integers = [int(''.join(map(str, flat_pixels[i:i+3]))) for i in range(0, len(flat_pixels), 3)]
    return large_integers

# Steps 4 & 5: Simulate ECC operations (simplified for demonstration)
def ecc_operations(large_integers, k=123456, Pb=789012):  # Example k and Pb
    kG = k * 2  # Simulating kG operation
    kPb = k * Pb  # Simulating kPb operation
    Pc = [(kPb + i) for i in large_integers]  # Simulate point addition with integers
    return Pc

# Step 6 adjustment: Ensure byte range conversion respects the original image size
def convert_to_byte_range(cipher_text, target_size):
    byte_array = [item % 256 for item in cipher_text]
    # Adjust the size of the byte_array to match target_size
    if len(byte_array) < target_size:
        # If too short, pad with zeros
        byte_array += [0] * (target_size - len(byte_array))
    else:
        # If too long, trim the excess
        byte_array = byte_array[:target_size]
    return byte_array

# Adjusted image reconstruction to handle mismatch in array size
def reconstruct_image(cipher_bytes, width, height, num_channels):
    expected_size = width * height * num_channels
    adjusted_cipher_bytes = np.array(cipher_bytes[:expected_size]).reshape((height, width, num_channels))
    reconstructed_image = Image.fromarray(adjusted_cipher_bytes.astype('uint8'))
    reconstructed_image.save('encrypted_image.png')

# Main function to execute the steps
def main(image_path):
    encrypted_pixels, num_channels, (width, height) = load_and_encrypt_image(image_path)
    large_integers = pixels_to_large_integers(encrypted_pixels)
    cipher_text = ecc_operations(large_integers)
    target_size = width * height * num_channels  # Calculate the expected size of the cipher_bytes
    cipher_bytes = convert_to_byte_range(cipher_text, target_size)  # Adjust the call
    reconstruct_image(cipher_bytes, width, height, num_channels)
    print("Image encryption and reconstruction complete.")


# Replace 'path_to_your_image.png' with the actual image path
main('../resources/Cat.jpg')
