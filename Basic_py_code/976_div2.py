# C - Bitwise Balancing
# t=int(input())
# for _ in range(t):
#     b,c,d=map(int,input().split())
#     a = b ^ d
#     if (a | b) - (a & c) == d:
#         print(a)
#     else:
#         print(-1)

# 	B - Brightness Begins
import math

t = int(input())
for _ in range(t):
    k = int(input())
    m = int(math.isqrt(k))  
    res = k + m
    if math.isqrt(res) > m:
        res += 1
    print(res)
