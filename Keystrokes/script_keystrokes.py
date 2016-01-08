import msvcrt
import time

def name():
    return 'keystrokes'

def collect(bits=50):
    arr = []
    for i in range(0, bits):
        start = int(round(time.time() * 1000))
        msvcrt.getch()
        end = int(round(time.time() * 1000))
        elapsed = end - start
        arr.append(0 if elapsed % 2 == 0 else 1)

    return arr
