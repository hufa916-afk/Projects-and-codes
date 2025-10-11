import hashlib
import random

def birthday():
    num_bits = 40
    n = 0
    hashes = {}
    while True:
        s = ''.join(chr(random.randint(32, 126)) for _ in range(10))
        hs = hashlib.sha1(s.encode('utf-8')).hexdigest()[:num_bits // 4]
        if hs in hashes:
            t = hashes[hs]
            return (s, t, n)
        else:
            hashes[hs] = s
            n += 1

print(birthday())
