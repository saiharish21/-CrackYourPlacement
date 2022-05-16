class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # l=sorted(nums)
        # for i in range(0,len(l)):
        #     if nums.count(l[i])>1:
        #         return l[i]
        
        tempset=set()
        for i in nums:
            if i in tempset:
                return i
            else:
                tempset.add(i)
