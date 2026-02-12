#leetcode problem solution
#problem number 1 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
print("Input your array length")
length=int(input())
arr=[]
for x in range(length):
    print("input array entry")
    value=int(input())
    arr.append(value)
print(arr)    
print("Input your Target:")
target=int(input())
for i in range(length):
    for j in range(i+1,length):
        if arr[i]+arr[j]==target:
           print([i,j])
#optimal solution
class Solution:
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in lookup:
                return [lookup[diff], i]
            

#problem remove element
class Solution:
    def removeElement(self, nums, val):
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
#longest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
        
        return strs[0]
            
 