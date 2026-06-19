class Solution:
    # Function to reverse digits of a number
    def reverseNumber(self, n):
        newnum = 0
        while n > 0:
            last = n % 10
            n //= 10
            newnum = newnum * 10 + last
        return newnum