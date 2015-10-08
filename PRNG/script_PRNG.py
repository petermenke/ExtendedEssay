import random

def name():
    return 'PRNG'

def collect(bits=50):
    arr = []
    for i in range(0, bits):
        arr.append(random.randint(0, 1))
    return arr
