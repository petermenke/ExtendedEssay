from VideoCapture import Device
import math

def name():
    return 'cam'

def collect(bits=50):
    came = Device()

    img = came.getImage()
    pix = img.load()
    width = img.size[0]
    height = img.size[1]

    size = int(round(math.sqrt(bits)))
    w_step = int(round(width / size))
    h_step = int(round(height / size))

    # will return a list of numbers as long as the next square
    arr = []
    for w in range(0, width, w_step):
        for h in range(0, height, h_step):
            cur_pix = pix[w, h]
            val = (cur_pix[0] + cur_pix[1] + cur_pix[2]) / 3
            arr.append(0 if val % 2 == 0 else 1)
    return arr[:bits]
