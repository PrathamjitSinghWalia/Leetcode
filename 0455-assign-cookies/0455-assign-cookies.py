class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        n=len(g)
        m=len(s)
        l=0
        r=0
        while l<m:
            if l<n and r<m:
                if s[r]>=g[l]:
                    l=l+1
                r=r+1
            else:
                break
        return l

        