import Elliptic
import os
import imgToDat


def encrypt_to_disk(name):
    p = 487
    a = 0
    b = 3

    document = "Assets/Output/inverse_ppp" + str(p) + ".txt"
    if not os.path.exists(document):
        Elliptic.calc_inverse(p, document)
    ECC = Elliptic.Elliptic(p, a, b, document)

    ECC.get_key()

    plain = imgToDat.compressedImg(name)
    return ECC.encrypt2(plain), plain
