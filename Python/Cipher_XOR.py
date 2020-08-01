#!/bin/python3
# Source: HackerRank - Medium (Bit Manipulation Topic)
import math
import os
import random
import re
import sys

# Complete the cipher function below.

def cipher(k, s, n):
    acc =0
    list_final= []
    for i in range(n):
        list_final.append(acc^int(s[i]))
        acc = acc^(list_final[-1])
        if i>=k-1:
            acc = acc^list_final[i-k+1]
    print(list_final)
    return ''.join([str(l) for l in list_final])


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = cipher(k, s, n)

    fptr.write(result + '\n')

    fptr.close()
