class Solution:

    def atMost(self, nums, k):
        left = 0
        count = 0
        ans = 0

        if k < 0:
            return 0

        for right in range(len(nums)):

            if nums[right] % 2 == 1:
                count += 1

            while count > k:
                if nums[left] % 2 == 1:
                    count -= 1
                left += 1

            ans += right - left + 1

        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)