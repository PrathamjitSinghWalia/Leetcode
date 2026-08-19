class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        ans=0

        for right in range(len(s)):
            curr=s[right]
            while curr in seen:
                seen.remove(s[left])
                left=left+1
            seen.add(curr)

            ans=max(ans,right-left +1)
        return ans
        