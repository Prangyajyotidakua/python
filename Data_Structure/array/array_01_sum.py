def sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return i , j
    return -1        


arr=[1,2,3,4,5]
target=6
val= sum(arr,target)   
print(val)         