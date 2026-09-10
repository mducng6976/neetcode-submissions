class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for n in s:
            if n.isalnum():
                temp += n.lower()

        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] == temp[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        

        