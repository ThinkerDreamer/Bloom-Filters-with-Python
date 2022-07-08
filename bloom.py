import encodings
import hashlib
import sys

registers = [False] * 32
print(registers)

posse = ["Angel", "Shae", "Josephine", "Hazem", "Adam"]

for person in posse:
    encodings = []
    encodings.append(hashlib.sha256(person.encode("utf-8")))
    encodings.append(hashlib.sha512(person.encode("utf-8")))
    encodings.append(hashlib.md5(person.encode("utf-8")))
    for encoding in encodings:
        reg = int.from_bytes(encoding.digest(),sys.byteorder) % 32
        registers[reg] = True

print(registers)
