# 1 -> 1 * 1 * 2 = 2
# 2 -> 2 * 2 * 2 = 8
# n -> n * n * 2 = 2n^2

import sys
import math

input = sys.stdin.readline

PI = math.pi
R = int(input())

print(R*R*PI)
print(R*R*2)