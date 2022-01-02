class Solution(object):
    def twoSum(self, nums, target):
        output= []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j]== target:
        #             output.append(i)
        #             output.append(j)
        # return output
                    return [i, j]


            
nums = [3,2,4]
target = 6
a= Solution()
print(a.twoSum(nums, target))
