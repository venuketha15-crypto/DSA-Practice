from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        prefix_index = {0: -1}
        prefix_sum = 0
        max_length = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in prefix_index:
                length = i - prefix_index[prefix_sum]
                max_length = max(max_length, length)
            else:
                prefix_index[prefix_sum] = i

        return max_length
