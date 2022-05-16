class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict={}
       for i in range(0,len(nums)):
            dict[nums[i]]=i
       for i in range(0,len(nums)):
            if target-nums[i] in dict:
                x=dict[target-nums[i]]
                if i!=x:
                    return [i,x]
        #    for i in range(0,len(nums)):
    #      if target-nums[i] in nums:
    #             x=nums.index(target-nums[i])
    #             if i!=x:
    #                 return [i,x]
