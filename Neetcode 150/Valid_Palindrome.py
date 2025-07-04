class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        s = s.lower()
         
        while (left <= right):
            # continue stmts are very important, we need to start the check process over
            # ex:   &&racecar -> two & in a row
            if (not( s[left].isalnum())):
                left += 1
                continue

            if (not( s[right].isalnum())):
                right -= 1
                continue

            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True
        
