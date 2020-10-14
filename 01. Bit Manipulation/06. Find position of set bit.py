# https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1

class Solution:
    
    def isValid(self,N):
        
        if N==0:
            return False
        
        temp = N
        cnt = 0
        while temp!=0:
            cnt+=1
            temp = temp&(temp-1)
            
            if(cnt==2):
                return False
        
        return True
            
    
    def findPosition(self, N):
        # code here 
        
        if not Solution.isValid(self,N):
            return -1
        else:
            for i in range(64):
                if N & (1<<i) > 0:
                    return (i+1)    