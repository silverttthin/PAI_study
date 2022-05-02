class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2) :
            #중복값 패스 -> 정렬된 배열일 때 사용 가능한듯 하다.
            if i>0 and nums[i] == nums[i - 1]: 
                continue
                
            left, right = i+1, len(nums) - 1
            
            while left<right:
                s = nums[i] + nums[left] + nums[right]
                
                if s>0: left += 1
                elif s<0 : right -= 1
                    
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left<right and nums[left] == nums[left + 1] :
                        left += 1
                        
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
            
        return result

a = Solution()
print(a.threeSum([-4,-1,-1,2,1,0]))