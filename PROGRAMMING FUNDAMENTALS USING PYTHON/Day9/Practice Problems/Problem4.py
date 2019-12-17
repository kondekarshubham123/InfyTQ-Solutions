#PF-Prac-4
def find_nine(nums):
    return 9 in nums and nums.index(9)<4

nums=[1,4,5,6]
print(find_nine(nums))