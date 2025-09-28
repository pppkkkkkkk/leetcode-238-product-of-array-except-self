class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = prod(nums)
        result = [0]*len(nums)
        if product > 0:
            for i,num in enumerate(nums):
                result[i] = product//num
        else:
            for i,num in enumerate(nums):
                result[i] = prod(nums[0:i]+nums[i+1:])
        return result
        # zCnt = 0
        # ans = [0]*len(nums)
        # for num in nums:
        #     if num == 0:
        #         zCnt +=1
        # if zCnt>1:
        #     return [0]*len(nums)
        # if zCnt == 1:
        #     tmp = 1
        #     pos0 = 0
        #     for i, num in enumerate(nums):
        #         if num != 0:
        #             tmp *= num
        #         else:
        #             pos0 = i
        #     ans[pos0] = tmp
        # else:
        #     tmp = 1
        #     for num in nums: 
        #         tmp *= num
            
        #     for i, num in enumerate(nums):
        #         ans[i] = tmp//num
        # return ans

