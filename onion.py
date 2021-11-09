#!/usr/bin/python
import base64
import uu

with open('output.txt', 'r')as f:
    data = f.readlines()

def dec64(data):
    for i in range(len(data)):
        data[i] = data[i].decode()
        print(data[i])

for i in range(len(data)):
    data[i] = uu.decode(data[i], 'output.txt')

with open('output.txt', 'w')as f:
    for adata in data:
        f.write(adata)
