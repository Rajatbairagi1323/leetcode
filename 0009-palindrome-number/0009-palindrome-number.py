class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x ==x[::-1]:
            return True
        else:
            return False
    def check(self):
        num=int(input("Enter a number: "))
        pal=self.ispalindrome(num)
        print(pal)