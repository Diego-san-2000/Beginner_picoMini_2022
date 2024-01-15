import hashlib

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

with open("dictionary.txt","r") as diccionario:
    for line in diccionario:
        clave = line.strip(" \n")
        print("Probando {}".format(clave))
        if( hash_pw(clave) == correct_pw_hash ):
            print("Flag encontrada: {}".format(clave))
            break