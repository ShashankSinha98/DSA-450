# https://practice.geeksforgeeks.org/problems/count-total-set-bits/0

dp = [0]*1000
for no in range(1000):
    cnt = 0
    temp = no
    while temp!=0:
        cnt+=1
        temp = temp & (temp-1)

        dp[no] = cnt

for i in range(1,1000):
    dp[i] += dp[i-1]


t = int(input())

while t!=0:
    t-=1

    n = int(input())
    print(dp[n])