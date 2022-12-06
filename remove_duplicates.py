class Solution:
    def removeDuplicates(self, nums):
        i = 0
        pop_counter = 0
        
        while i < len(nums):
            if nums[i] == "_":
                i +=1   
            elif i > 1 and (nums[i]==nums[i-1]==nums[i-2]):
                print(nums)
                nums.pop(i)
                pop_counter +=1  
                nums.append("_")
            else:
                i+=1
        
        print(nums)
        return len(nums)-pop_counter
        
        
        
        
obj = Solution()



nums = [1,1,1,2,2,3] #5, nums = [1,1,2,2,3,_]
nums1 = [0,0,0,0,0]

print(obj.removeDuplicates(nums1))