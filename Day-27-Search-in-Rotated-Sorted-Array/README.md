# Day 27 of My DSA Journey 🚀

## Problem 27: Search in Rotated Sorted Array

### Difficulty
Medium

### Problem Link

[LeetCode - Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

### Problem Statement

There is an integer array `nums` sorted in ascending order with distinct values.

Before being passed to your function, `nums` is rotated at an unknown pivot.

Given the array `nums` after rotation and an integer `target`, return the index of `target`.

If the target does not exist, return:

```text
-1
```

You must write an algorithm with:

```text
O(log n)
```

time complexity.

---

## Optimized Approach (Binary Search)

- Use Binary Search on the rotated array.
- Find the middle element.
- Determine which half of the array is sorted.
- Check whether the target lies inside the sorted half.
- If yes, search that half.
- Otherwise, search the other half.
- Continue until the target is found or the search space becomes empty.

---

## Example

### Input

```text
nums = [4,5,6,7,0,1,2]
target = 0
```

---

### Step 1

```text
left = 0
right = 6
```

Find middle:

```text
mid = (0 + 6) // 2 = 3
```

Middle element:

```text
nums[mid] = 7
```

Left half:

```text
[4,5,6,7]
```

is sorted.

Target:

```text
0
```

is not inside the left half.

Move:

```text
left = mid + 1
```

Now:

```text
left = 4
right = 6
```

---

### Step 2

Find middle:

```text
mid = (4 + 6) // 2 = 5
```

Middle element:

```text
nums[mid] = 1
```

Left half:

```text
[0,1]
```

is sorted.

Target:

```text
0
```

lies inside this half.

Move:

```text
right = mid - 1
```

Now:

```text
left = 4
right = 4
```

---

### Step 3

Find middle:

```text
mid = 4
```

Middle element:

```text
nums[mid] = 0
```

Target found.

Return:

```text
4
```

---

## Final Output

```text
4
```

---

## Explanation

The key idea is to identify which half of the rotated array is sorted.

Once the sorted half is identified, check whether the target lies inside that half.

If it does, continue searching there.

Otherwise, search the other half.

By eliminating half of the search space in every iteration, Binary Search efficiently finds the target.

---

## Time Complexity

```text
O(log n)
```

Reason:

- Half of the search space is discarded in every iteration.

---

## Space Complexity

```text
O(1)
```

Reason:

- Only a few variables are used.

---

## What I Learned

- How Binary Search works on rotated sorted arrays.
- How to identify the sorted half of the array.
- How to determine which half contains the target.
- How to eliminate half of the search space efficiently.
- Why this approach achieves O(log n) time complexity.
- How rotated array searching differs from normal Binary Search.

---

✅ Problem Solved: Search in Rotated Sorted Array (LeetCode #33)

🐍 Language: Python

📅 Day 27 of Daily DSA Practice
