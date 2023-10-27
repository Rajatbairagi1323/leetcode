class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                output.append(nums[:])
            else:
                for i in range(start, end):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1, end)
                    nums[start], nums[i] = nums[i], nums[start]

        output = []
        backtrack(0, len(nums))
        return output

     

