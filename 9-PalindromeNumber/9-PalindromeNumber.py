# Last updated: 5/25/2025, 10:27:50 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[:] == str(x)[::-1]