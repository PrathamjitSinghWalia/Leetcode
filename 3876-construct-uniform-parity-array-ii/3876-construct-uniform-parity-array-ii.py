class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1) % 2 == 1 or all(num % 2 == 0 for num in nums1)