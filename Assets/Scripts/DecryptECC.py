import Elliptic
import os


def decrypt_to_pic(c):
    p = 487
    a = 0
    b = 3

    document = "Assets/Output/inverse_ppp" + str(p) + ".txt"
    if not os.path.exists(document):
        Elliptic.calc_inverse(p, document)
    ECC = Elliptic.Elliptic(p, a, b, document)

    ECC.get_key()
    de = ECC.decrypt2(c)
    return de
