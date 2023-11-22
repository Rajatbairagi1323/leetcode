class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = []
        for number in nums:
            if number in result:
                result.remove(number)
            else:
                result.append(number)
        return result[0]
        