#!/usr/bin/python
import base64
import sys

argv = sys.argv

def dec64(data):
    for i in range(len(data)):
        data[i] = base64.b64decode(data[i]).decode()
        with open('output.txt', 'w')as f:
            for i in range(len(data)):
                f.write(data[i])

with open(argv[1], 'r')as f:
    data = f.readlines()

dec64(data)

