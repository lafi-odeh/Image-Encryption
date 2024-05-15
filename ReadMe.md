# Secure-Image-Chatting-System

This project is a preview of a secure chatting system for images. To securely encrypt and decrypt images, Elliptic Curve Cryptography is used.

For each image, an object "Elliptic" is created, with data members "a" and "b" corresponding to coefficients in the elliptic curve function. Data member "p" is the prime number defining the finite field. "xg" and "yg" are the coordinates of the point G.

Pixel grouping is done before encryption.

The image is then compressed to a size of 146 x 96. The image is encrypted using a random point on the curve and the derived public key of the sender.

Entropy analysis and histogram analysis are then used to measure the security of the encryption process.

Decryption is done by reversing the encryption process.

An individual file is made for the "Elliptic" class and the encrypt and decrypt functions. `Main.py` can be used to test encrypting and decrypting on certain images.

## Setup Instructions

### Requirements

- Python 3.6 or higher
- Virtualenv

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/Secure-Image-Chatting-System.git
   cd Secure-Image-Chatting-System
   ```

2. **Set up a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install dependencies:**

   Ensure you have a `requirements.txt` file in the project directory. Create it if it doesn't exist and add the required packages.

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```sh
   python Main.py
   ```

### Creating `requirements.txt`

If you don't have a `requirements.txt` file, you can create one by running:

```sh
pip freeze > requirements.txt
```

This will capture the currently installed packages in your environment and save them to `requirements.txt`.
