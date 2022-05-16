class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
        # c0,c1,c2=0,0,0
        # for i in range(0,len(nums)):
        #     if nums[i]==0:
        #         c0+=1
        #     elif nums[i]==1:
        #         c1+=1
        #     else:
        #         c2+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        
