class Solution:
       def letterCombinations(self, digits):
        if not digits:
            return []

        digits_in_letters = {'2': 'abc',
                             '3': 'def',
                             '4': 'ghi',
                             '5': 'jkl',
                             '6': 'mno',
                             '7': 'pqrs',
                             '8': 'tuv',
                             '9': 'wxyz'}

        result = ['']

        for digit in digits:
            letters = digits_in_letters[digit]

            new_result = []

            for i in result:
                for j in letters:
                    new_result.append(i + j)

            result = new_result

        return result
