# Day 44 of My DSA Journey 🚀

## Problem 44: Max Consecutive Ones III

### Difficulty
Medium

### Problem Link

[LeetCode - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

---

## Problem Statement

Given a binary array `nums` and an integer `k`, return the **maximum number of consecutive `1`s** in the array if you can flip at most `k` `0`s.

---

## Optimized Approach (Sliding Window)

- Initialize two pointers:
  - `left`
  - `right`
- Keep track of the number of `0`s inside the current window.
- Expand the window by moving the `right` pointer.
- If the number of `0`s becomes greater than `k`, shrink the window by moving the `left` pointer until the window becomes valid again.
- Update the maximum window length after every valid window.

---

## Example

### Input

```text
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

---

### Sliding Window Process

```text
Window: [1]
Zero Count = 0
Length = 1
```

```text
Window: [1,1,1]
Zero Count = 0
Length = 3
```

```text
Window: [1,1,1,0]
Zero Count = 1
Length = 4
```

```text
Window: [1,1,1,0,0]
Zero Count = 2
Length = 5
```

```text
Window: [1,1,1,0,0,0]
Zero Count = 3 ❌

Too many zeros.
Shrink the window from the left until Zero Count = 2.
```

Continue expanding and shrinking until the end of the array.

---

## Final Output

```text
6
```

---

## Explanation

The Sliding Window keeps track of the current window.

- Expand the window by moving the `right` pointer.
- Count the number of zeros inside the window.
- If the number of zeros exceeds `k`, move the `left` pointer until the window becomes valid again.
- Update the maximum window length whenever the window is valid.

---

## Time Complexity

```text
O(n)
```

### Reason

Each element enters and leaves the sliding window at most once.

---

## Space Complexity

```text
O(1)
```

### Reason

Only three variables (`left`, `zeroCount`, and `maxLength`) are used.

---

## What I Learned

- How Variable Size Sliding Window works.
- How to maintain a valid window.
- Why we count the number of zeros in the current window.
- When to expand and shrink the window.
- How to find the maximum window length in **O(n)** time.

---

✅ Problem Solved: Max Consecutive Ones III (LeetCode #1004)

🐍 Language: Python

📅 Day 44 of Daily DSA Practice
