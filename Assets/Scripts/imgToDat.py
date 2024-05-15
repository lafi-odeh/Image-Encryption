import numpy as np
from PIL import Image

def compressedImg(filePath, augment=0):
    img = Image.open(filePath)

    imgCompressed = img.resize((146, 96))

    if augment == -1:
        return np.array(list(img.getdata())).reshape(-1)
    else:
        return np.array(list(imgCompressed.getdata())).reshape(-1)


def restoreImg(decrypted, file_name, dimSize=(146,96)):
    width = dimSize[0]
    height = dimSize[1]

    temp = np.array(decrypted).reshape((height, width, 3))

    imgRecovered = Image.fromarray(temp)
    imgRecovered.save(file_name, format='png')

def restoreImg2(encrypted, file_name, dimSize=(146,96)):

    encrypted = np.array(encrypted)
    imgRecovered = Image.fromarray(encrypted)
    print(imgRecovered)
    imgRecovered.save(file_name, format='png')

