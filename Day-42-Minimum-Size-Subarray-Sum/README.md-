# Day 42 of My DSA Journey 🚀

## Problem 42: Minimum Size Subarray Sum

### Difficulty
Medium

### Problem Link

[LeetCode - Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

---

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimum length** of a contiguous subarray whose sum is **greater than or equal to** `target`.

If there is no such subarray, return `0`.

---

## Optimized Approach (Sliding Window)

- Initialize two pointers:
  - `left`
  - `right`
- Expand the window by moving the `right` pointer.
- Keep adding elements to the current window sum.
- Once the current sum becomes greater than or equal to the target:
  - Update the minimum window length.
  - Shrink the window by removing the leftmost element.
- Continue until all elements are processed.
- Return the minimum window length.

---

## Example

### Input

```text
target = 7
nums = [2,3,1,2,4,3]
```

---

### Sliding Window Process

```text
Window: [2]
Sum = 2

Window: [2,3]
Sum = 5

Window: [2,3,1]
Sum = 6

Window: [2,3,1,2]
Sum = 8 ✅
Length = 4
```

Shrink the window:

```text
Window: [3,1,2]
Sum = 6
```

Expand again:

```text
Window: [3,1,2,4]
Sum = 10 ✅
Length = 4
```

Shrink again:

```text
Window: [1,2,4]
Sum = 7 ✅
Length = 3
```

Shrink again:

```text
Window: [2,4]
Sum = 6
```

Expand again:

```text
Window: [2,4,3]
Sum = 9 ✅
Length = 3
```

Shrink again:

```text
Window: [4,3]
Sum = 7 ✅
Length = 2
```

---

## Final Output

```text
2
```

The smallest valid subarray is:

```text
[4,3]
```

---

## Explanation

The Sliding Window technique maintains a continuous window of elements.

- The `right` pointer expands the window.
- The `left` pointer shrinks the window whenever the current sum is greater than or equal to the target.
- This avoids checking every possible subarray and gives the optimal solution.

---

## Time Complexity

```text
O(n)
```

### Reason

Each element enters the window once and leaves the window at most once.

---

## Space Complexity

```text
O(1)
```

### Reason

Only a few variables (`left`, `right`, `currentSum`, and `minimum`) are used.

---

## What I Learned

- How the Sliding Window technique works.
- When to expand and shrink the window.
- Why we calculate the window length using `right - left + 1`.
- Why Sliding Window is more efficient than the brute force approach.
- How to solve this problem in **O(n)** time and **O(1)** space.

---

✅ Problem Solved: Minimum Size Subarray Sum (LeetCode #209)

🐍 Language: Python

📅 Day 42 of Daily DSA Practice
