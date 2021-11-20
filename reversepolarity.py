#!/usr/bin/python3
import binascii

pb = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"

for i in range(0, len(pb), 8):
    num = pb[0+i:8+i]
    num = int(num, 2)
    num = hex(num)
    print(num)

    


print(len(pb))


