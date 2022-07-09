import hashlib
import sys

registers = [False] * 32
print(registers)
hashers = [hashlib.sha256, hashlib.sha512, hashlib.md5]

def hash_and_add(data):
    for h in hashers:
        result = h(data.encode('utf-8'))
        reg = int.from_bytes(result.digest(),sys.byteorder) % 32
        registers[reg] = True

def hash_and_check(data):
    results = []
    for h in hashers:
        result = h(data.encode('utf-8'))
        reg = int.from_bytes(result.digest(),sys.byteorder) % 32
        results.append(registers[reg])
    return not False in set(results)

posse = ["Angel", "Shae", "Josephine", "Hazem", "Adam"]
for person in posse:
    hash_and_add(person)

# print(registers)

test_value = input("Enter a test value: ")
print(hash_and_check(test_value))