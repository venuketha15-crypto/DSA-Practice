# Day 4 of My DSA Journey 🚀

## Problem 4: Median of Two Sorted Arrays

### Difficulty
Hard

### Problem Link

https://leetcode.com/problems/median-of-two-sorted-arrays/

### Problem Statement

Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(min(m,n))).

### Brute Force Approach

- Merge both sorted arrays into a single sorted array.
- Find the median from the merged array.
- This approach is simple and easy to understand.
- However, it requires extra space and takes more time.

### Time Complexity of Brute Force

O(m + n)

where:

- m = length of nums1
- n = length of nums2

### Optimized Approach (Binary Search)

- I applied Binary Search on the smaller array.
- I partitioned both arrays into left and right halves.
- I compared the boundary elements of the partitions.
- If the partition was invalid, I adjusted the Binary Search range.
- Once a valid partition was found, I calculated the median.
- This approach avoids merging the arrays and achieves logarithmic time complexity.

### Example

Input:

nums1 = [1,3]

nums2 = [2]

Step 1:

Find lengths of both arrays.

m = 2

n = 1

Since nums1 is larger, swap the arrays.

nums1 = [2]

nums2 = [1,3]

Now:

m = 1

n = 2

Step 2:

Initialize Binary Search.

low = 0

high = 1

Step 3:

Calculate partitions.

c1 = (low + high) // 2

c1 = (0 + 1) // 2

c1 = 0

c2 = (m + n + 1) // 2 - c1

c2 = (1 + 2 + 1) // 2 - 0

c2 = 2

Step 4:

Find boundary elements.

l1 = -∞

r1 = 2

l2 = 3

r2 = +∞

Step 5:

Check partition condition.

l1 <= r2

-∞ <= +∞ ✅

l2 <= r1

3 <= 2 ❌

Partition is invalid.

Move Binary Search to the right.

low = c1 + 1

low = 1

Step 6:

Calculate partitions again.

c1 = 1

c2 = 1

Step 7:

Find boundary elements.

l1 = 2

r1 = +∞

l2 = 1

r2 = 3

Step 8:

Check partition condition.

l1 <= r2

2 <= 3 ✅

l2 <= r1

1 <= +∞ ✅

Valid partition found.

Step 9:

Total number of elements = 3 (odd)

Median = max(l1, l2)

Median = max(2, 1)

Median = 2

Output:

2.0

Explanation:

A valid partition is found such that:

l1 <= r2

and

l2 <= r1

Since the total number of elements is odd,

Median = max(l1, l2)

Median = 2

Verification:

Combined sorted array = [1,2,3]

The middle element is 2.

### Time Complexity

O(log(min(m,n)))

where:

- m = length of nums1
- n = length of nums2

Binary Search is performed on the smaller array.

### Space Complexity

O(1)

No extra array is created.

### What I Learned

- How to apply Binary Search on arrays in a non-traditional way.
- How array partitioning works.
- How to find the median without merging arrays.
- How to optimize a solution from O(m+n) to O(log(min(m,n))).
- Why choosing the smaller array for Binary Search is important.

✅ Problem Solved: Median of Two Sorted Arrays (LeetCode #4)

🐍 Language: Python

📅 Day 4 of Daily DSA Practice
