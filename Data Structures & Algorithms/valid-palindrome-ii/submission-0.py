class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                L, R = s[l+1:r+1], s[l:r]
                return (L==L[::-1] or R==R[::-1])
            l, r = l+1, r-1
        return True