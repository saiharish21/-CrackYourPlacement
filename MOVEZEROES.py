class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j,c=-1,0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                j=j+1
                nums[j]=nums[i]
            else:
                 c+=1
        for i in range(len(nums)-c , len(nums)):
            nums[i]=0
        #TWO POINTER APPROACH
            
        """
        Do not return anything, modify nums in-place instead.
        """
        
