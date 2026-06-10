# Day 12 of My DSA Journey 🚀

## Problem 12: Merge Sorted Array

### Difficulty
Easy

### Problem Link

[LeetCode - Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

### Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`.

Merge `nums2` into `nums1` as one sorted array.

The final sorted array should be stored inside `nums1`.

### Brute Force Approach

- Copy all elements of `nums2` into the empty positions of `nums1`.
- Sort the entire `nums1` array.
- The sorted array becomes the final merged result.

### Time Complexity of Brute Force

O((m + n) log(m + n))

Sorting the merged array takes O((m + n) log(m + n)) time.

### Space Complexity of Brute Force

O(1)

The merge is performed in-place.

### Optimized Approach (Three Pointers)

- Start from the end of both arrays.
- Use three pointers:
  - `i` → last valid element in `nums1`
  - `j` → last element in `nums2`
  - `k` → last position in `nums1`
- Compare `nums1[i]` and `nums2[j]`.
- Place the larger element at position `k`.
- Move the corresponding pointer backward.
- Continue until all elements of `nums2` are placed.

### Example

Input:

```text
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

Initial:

```text
i = 2  -> nums1[i] = 3
j = 2  -> nums2[j] = 6
k = 5
```

### Step 1

Compare:

```text
3 vs 6
```

6 is larger.

Place 6 at index 5.

```text
[1,2,3,0,0,6]
```

Move:

```text
j = 1
k = 4
```

### Step 2

Compare:

```text
3 vs 5
```

5 is larger.

Place 5 at index 4.

```text
[1,2,3,0,5,6]
```

Move:

```text
j = 0
k = 3
```

### Step 3

Compare:

```text
3 vs 2
```

3 is larger.

Place 3 at index 3.

```text
[1,2,3,3,5,6]
```

Move:

```text
i = 1
k = 2
```

### Step 4

Compare:

```text
2 vs 2
```

Place 2.

```text
[1,2,2,3,5,6]
```

Move:

```text
j = -1
```

The main loop ends.

### Final Result

```text
[1,2,2,3,5,6]
```

Output:

```text
[1,2,2,3,5,6]
```

### Explanation

The key idea is to merge from the end of the arrays.

Since `nums1` already has enough empty space, we place the largest element at the last available position.

This prevents shifting elements and allows us to merge efficiently.

For:

```text
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
```

The merged sorted array becomes:

```text
[1,2,2,3,5,6]
```

Using three pointers helps us process every element only once.

### Time Complexity

O(m + n)

Each element is processed at most once.

### Space Complexity

O(1)

Only a few pointers are used.

### What I Learned

- How to merge two sorted arrays efficiently.
- Why merging from the end avoids shifting elements.
- How the Three Pointers technique works.
- The difference between a brute-force and optimized solution.
- How to optimize a solution from O((m+n) log(m+n)) to O(m+n).
- How in-place algorithms help reduce extra memory usage.

✅ Problem Solved: Merge Sorted Array (LeetCode #88)

🐍 Language: Python

📅 Day 12 of Daily DSA Practice
