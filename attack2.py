import codecs
import time
import hashlib

start_time = time.time()
with open('base-hashed-passwords.csv', 'r') as f:
    datafile = f.readlines()
    for cainline in codecs.open("cain.txt", 'rb', encoding='utf-8', errors='ignore'):
        hash = hashlib.sha256(cainline.strip().encode('utf-8')).hexdigest()
        for line in datafile:
            if hash in line:
                print(line)
                print(cainline)
                break
elapsed_time = time.time() - start_time
print(elapsed_time)
