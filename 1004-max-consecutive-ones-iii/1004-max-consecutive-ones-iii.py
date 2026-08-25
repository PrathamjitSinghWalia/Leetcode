class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=0
        zeros=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros=zeros+1
            while zeros>k:
                if nums[left]==0:
                    zeros=zeros-1
                left=left+1
            count=max(count,right-left+1)
        return count


        