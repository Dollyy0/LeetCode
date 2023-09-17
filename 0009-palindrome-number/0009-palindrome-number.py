class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int =str(x)
        sliced_str = str_int[::-1]
        if sliced_str == str_int:
            return True
        else:
            return False
        