from faker import Faker
fake = Faker('fr_FR')

f = open("base-hashed-passwords.csv", "a")
for _ in range(500):
    f.write(fake.ascii_free_email())
    f.write(";")

    f.write(fake.sha256(raw_output=False))
    f.write("\n")

f.close()
