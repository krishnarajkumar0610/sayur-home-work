def sumAll(nums):
    if len(nums)==1:
        return nums[0]
    else:
        return nums[0]+sumAll(nums[1:])
 
nums= [1,2,3,4,5]
print(sumAll(nums))