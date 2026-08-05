class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        j=0
        first=strs[0]
        for i in range(len(first)):
             for j in range(1,len(strs)):
                if i>=len(strs[j]):
                     return first[:i]
                elif first[i]!=strs[j][i]:
                    return first[:i]

        return first
