class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        currentSum = 0
        minimum = float("inf")

        for right in range(len(nums)):

            currentSum += nums[right]

            while currentSum >= target:

                minimum = min(minimum, right - left + 1)

                currentSum -= nums[left]
                left += 1

        if minimum == float("inf"):
            return 0

        return minimum
