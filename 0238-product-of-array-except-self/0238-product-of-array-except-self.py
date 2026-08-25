class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[]
        leftprod=1
        rightprod=1
        for i in range(len(nums)):
            answer.append(leftprod)
            leftprod=leftprod*nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            answer[i]=answer[i]*rightprod
            rightprod=rightprod*nums[i]

        return answer

        