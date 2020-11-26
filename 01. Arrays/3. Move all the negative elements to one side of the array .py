#arr = [int(i) for i in input().split()]

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

left = 0
right = len(arr)-1

while left<=right:
    if arr[left]>0 and arr[right]<0:
        arr[left], arr[right] = arr[right], arr[left]
        right-=1
        left+=1
    
    elif arr[left]>0:
        right-=1
    
    elif arr[right]<0:
        left+=1
    
    else:
        left+=1
        right-=1

print(arr)