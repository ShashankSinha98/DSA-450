# https://practice.geeksforgeeks.org/problems/bit-difference/0

def solve(a,b):
    
    cnt = 0
    for i in range(64):
        if a&(1<<i) != b&(1<<i):
            cnt += 1
    
    return cnt



t = int(input())

while t!=0:
    t-=1
    a,b = [int(i) for i in input().split()]
    
    print(solve(a,b))