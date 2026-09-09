class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""

        for t in s:
            if t.isalnum():
                temp += t.lower()

        left = 0
        right = len(temp) - 1

        while left < right:
            if temp[left] == temp[right]:
                left += 1
                right -= 1
            else:
                return False

        return True