def maxSubArraySum(a,size):
    ##Your code here
    maxSoFar = max(a)
    maxTillNow = 0
    
    for i in a:
        maxTillNow += i
        
        if maxTillNow > maxSoFar:
            maxSoFar = maxTillNow
        
        if maxTillNow < 0:
            maxTillNow = 0
            
    return maxSoFar