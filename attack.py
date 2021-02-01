import codecs
import time

start_time = time.time()
with open('base-hashed-passwords.csv', 'r') as f:
    datafile = f.readlines()
    for rainbowline in codecs.open("cain.csv", 'rb', encoding='utf-8', errors='ignore'):
        rb = rainbowline.strip().split("\t")
        for line in datafile:
            if rb[0] in line:
                print(line.strip().split(";")[0])
                print(rainbowline.strip().split("\t")[1])
                break
elapsed_time = time.time() - start_time
print(elapsed_time)
