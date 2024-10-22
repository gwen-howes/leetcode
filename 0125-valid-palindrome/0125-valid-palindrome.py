class Solution:
    def isPalindrome(self, s: str) -> bool:
        sClean = ''.join(char for char in s if char.isalnum()).lower()

        i, j = 0, len(sClean)-1

        while(i < j):
            if sClean[i] != sClean[j]:
                return False
            
            i += 1
            j -= 1

        return True