class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for n in s:
            if n.isalnum():
                temp += n.lower()

        if temp == temp[::-1]:
            return True
        return False
        
