# https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1

class Solution:
	def singleNumber(self, nums):
		# Code here
		
		xor_val = 0
		for i in nums:
		    xor_val = xor_val ^ i
		    
		temp = xor_val
		pos = 0
		while temp!=0:
		    if temp & 1 == 1:
		        break
		    pos+=1
		    temp=temp>>1
		
		firstNum = 0
		for no in nums:
		    if no & (1<<pos)>0:
		        firstNum = firstNum ^ no
		
		secondNum = xor_val^firstNum
		ans = [firstNum,secondNum]
		ans.sort()
		return ans