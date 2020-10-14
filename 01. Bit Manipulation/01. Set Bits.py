# https://practice.geeksforgeeks.org/problems/set-bits0143/1

class Solution:
	def setBits(self, N):
		# code here
		cnt = 0
		
		while(N!=0):
		    N = N & (N-1)
		    cnt+=1
		
		return cnt