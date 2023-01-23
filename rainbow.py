import csv
import hashlib
import codecs


# create rainbow table file
output = open("cain.csv", "a")
for line in codecs.open("cain.txt", 'rb', encoding='utf-8', errors='ignore'):
    m = hashlib.sha256(line.strip().encode('utf-8')).hexdigest()
    output.write(m)
    output.write("\t")
    output.write(line.strip())
    output.write("\n")

output.close()
