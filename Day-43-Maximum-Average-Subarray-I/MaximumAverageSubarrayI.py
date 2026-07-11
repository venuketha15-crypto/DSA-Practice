class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        currentSum = sum(nums[:k])
        maxSum = currentSum

        for right in range(k, len(nums)):
            currentSum += nums[right]
            currentSum -= nums[right - k]

            maxSum = max(maxSum, currentSum)

        return maxSum / k
