def solve(x,y,l,r):

    ans = y & ((2**r)-1)
    ans = ans & ((-1)<<(l-1))

    return x | ans



x = 8
y = 7
l,r = 1,2

print(solve(x,y,l,r))
