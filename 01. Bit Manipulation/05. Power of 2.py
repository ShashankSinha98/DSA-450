
def solve(n):

    if n==0:
        return "NO"

    cnt = 0
    while n!=0:
        cnt+=1
        n = n&(n-1)

        if(cnt==2):
            return "NO"
    
    return "YES"


t = int(input())

while t!=0:
    t-=1

    n = int(input())
    print(solve(n))

    