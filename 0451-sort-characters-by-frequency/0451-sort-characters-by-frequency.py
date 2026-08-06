class Solution:
    def frequencySort(self, s: str) -> str:
        sort={}
        sort2={}
        answer=""
        for i in range(len(s)):
            if s[i] in  sort:
                sort[s[i]]=sort[s[i]]+1
            else:
                sort[s[i]]=1
        sort2=sorted(sort.items(), key=lambda x: x[1], reverse=True)

        for ch,freq in sort2:
            answer=answer+ch*freq
        return answer



