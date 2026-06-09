# Day 11 of My DSA Journey 🚀

## Problem 11: Remove Duplicates from Sorted Array

### Difficulty
Easy

### Problem Link

https://leetcode.com/problems/remove-duplicates-from-sorted-array/

### Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.

Return the number of unique elements.

### Brute Force Approach

- Start from the second element of the array.
- Compare the current element with the previous element.
- If both elements are the same, remove the duplicate element using `remove()`.
- Otherwise, move to the next element.
- Continue until the end of the array.

### Time Complexity of Brute Force

O(n²)

Removing an element from a list requires shifting all elements to the left.

In the worst case, multiple removals occur, leading to quadratic time complexity.

### Space Complexity of Brute Force

O(1)

No extra data structure is used.

### Optimized Approach (Two Pointers)

- Use two pointers: `slow` and `fast`.
- `slow` points to the last unique element found.
- `fast` scans the array from left to right.
- Whenever a new unique element is found:
  - Move `slow` one step forward.
  - Copy the unique element to `nums[slow]`.
- At the end, the first `slow + 1` elements contain all unique values.

### Example

Input:

```text
nums = [1,1,2,2,3,4,4]
```

Initial:

```text
slow = 0
fast = 1
```

Array:

```text
[1,1,2,2,3,4,4]
```

### Step 1

```text
nums[fast] = 1
nums[slow] = 1
```

Duplicate found.

```text
slow = 0
```

Move `fast`.

### Step 2

```text
nums[fast] = 2
nums[slow] = 1
```

Unique element found.

```text
slow = 1
nums[1] = 2
```

Array becomes:

```text
[1,2,2,2,3,4,4]
```

### Step 3

```text
nums[fast] = 2
nums[slow] = 2
```

Duplicate found.

Move `fast`.

### Step 4

```text
nums[fast] = 3
nums[slow] = 2
```

Unique element found.

```text
slow = 2
nums[2] = 3
```

Array becomes:

```text
[1,2,3,2,3,4,4]
```

### Step 5

```text
nums[fast] = 4
nums[slow] = 3
```

Unique element found.

```text
slow = 3
nums[3] = 4
```

Array becomes:

```text
[1,2,3,4,3,4,4]
```

Final unique elements:

```text
[1,2,3,4]
```

Length:

```text
4
```

Output:

```text
4
```

### Explanation

The array is already sorted, so duplicate elements appear next to each other.

The `fast` pointer scans every element.

Whenever a new unique element is found, it is placed immediately after the last unique element tracked by the `slow` pointer.

This allows us to remove duplicates in-place without using extra memory.

For:

```text
[1,1,2,2,3,4,4]
```

The unique elements are:

```text
[1,2,3,4]
```

So the answer is:

```text
4
```

### Time Complexity

O(n)

where n is the length of the array.

Each element is visited exactly once.

### Space Complexity

O(1)

Only two pointers are used.

### What I Learned

- How the Two Pointers technique works.
- The difference between brute-force and optimized approaches.
- How to modify an array in-place.
- Why sorted arrays make duplicate removal easier.
- How to optimize a solution from O(n²) to O(n).

✅ Problem Solved: Remove Duplicates from Sorted Array (LeetCode #26)

🐍 Language: Python

📅 Day 11 of Daily DSA Practice
