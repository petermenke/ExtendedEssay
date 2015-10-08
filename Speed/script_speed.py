import time

def name():
    return 'speed'

def collect(bits=50):
    arr = []
    for t in range(0, bits):
        current_milli_time = lambda: int(round(time.time() * 1000))
        initial = current_milli_time()
        i = 0
        while current_milli_time() == initial:
            i += 1
        arr.append(0 if i % 2 == 0 else 1)
    return arr
