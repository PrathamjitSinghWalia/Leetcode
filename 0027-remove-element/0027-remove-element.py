class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new=[]
        for i in range (len(nums)):
            if nums[i]!=val:
                new.append(nums[i])
        k=len(new)

        for i in range(k):
            nums[i]=new[i]
        return k

        