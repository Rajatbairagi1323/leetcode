class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        n=len(nums)
        for i in nums:
            dict1[i]=dict1.get(i,0)+1
            if dict1[i]>n//2:
                return i