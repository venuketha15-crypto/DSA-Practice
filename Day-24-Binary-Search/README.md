# Day 24 of My DSA Journey 🚀

## Problem 24: Binary Search

### Difficulty
Easy

### Problem Link

[LeetCode - Binary Search](https://leetcode.com/problems/binary-search/)

### Problem Statement

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search for `target`.

If `target` exists, return its index.

Otherwise, return:

```text
-1
```

You must write an algorithm with:

```text
O(log n)
```

runtime complexity.

---

## Optimized Approach (Binary Search)

- Initialize two pointers:
  - `left` at the beginning of the array.
  - `right` at the end of the array.
- Find the middle element.
- If the middle element equals the target, return its index.
- If the target is smaller, search the left half.
- If the target is larger, search the right half.
- Repeat until the target is found or the search space becomes empty.

---

## Example

### Input

```text
nums = [-1,0,3,5,9,12]
target = 9
```

---

### Step 1

```text
left = 0
right = 5
```

Find middle:

```text
mid = (0 + 5) // 2 = 2
```

Middle element:

```text
nums[2] = 3
```

Compare:

```text
9 > 3
```

Search right half.

Update:

```text
left = 3
```

---

### Step 2

```text
left = 3
right = 5
```

Find middle:

```text
mid = (3 + 5) // 2 = 4
```

Middle element:

```text
nums[4] = 9
```

Compare:

```text
9 == 9
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

The key idea is to eliminate half of the search space in every iteration.

Instead of checking every element one by one, Binary Search compares the target with the middle element and decides which half can be ignored.

This significantly reduces the number of comparisons.

---

## Time Complexity

```text
O(log n)
```

Reason:

- The search space is reduced by half in every iteration.

Example:

```text
16 elements → 8 → 4 → 2 → 1
```

---

## Space Complexity

```text
O(1)
```

Reason:

- Only a few variables are used.

---

## What I Learned

- How Binary Search works.
- How to calculate the middle index.
- How to eliminate half of the search space.
- How to use left and right pointers efficiently.
- Why Binary Search achieves O(log n) time complexity.
- Why Binary Search requires a sorted array.

---

✅ Problem Solved: Binary Search (LeetCode #704)

🐍 Language: Python

📅 Day 24 of Daily DSA Practice
