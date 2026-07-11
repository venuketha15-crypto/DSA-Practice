# Day 43 of My DSA Journey 🚀

## Problem 43: Maximum Average Subarray I

### Difficulty
Easy

### Problem Link

[LeetCode - Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

---

## Problem Statement

You are given an integer array `nums` consisting of `n` elements and an integer `k`.

Find the **maximum average value** of any contiguous subarray of length `k` and return it.

---

## Optimized Approach (Fixed Size Sliding Window)

- Calculate the sum of the first `k` elements.
- Store it as the current maximum sum.
- Slide the window one element at a time.
- Add the new element entering the window.
- Remove the old element leaving the window.
- Update the maximum sum whenever a larger sum is found.
- Return the maximum average.

---

## Example

### Input

```text
nums = [1,12,-5,-6,50,3]
k = 4
```

---

### Initial Window

```text
[1,12,-5,-6]

Sum = 2
Max Sum = 2
```

---

### Slide Window Once

```text
Remove: 1
Add: 50

Window:

[12,-5,-6,50]

Sum = 51
Max Sum = 51
```

---

### Slide Window Again

```text
Remove: 12
Add: 3

Window:

[-5,-6,50,3]

Sum = 42
Max Sum = 51
```

---

## Final Output

```text
12.75
```

---

## Explanation

Instead of calculating the sum of every window from scratch, we reuse the previous window's sum.

When the window moves:

- Add the new element entering the window.
- Remove the old element leaving the window.

This reduces unnecessary calculations and makes the solution efficient.

---

## Time Complexity

```text
O(n)
```

### Reason

Each element is added to the window once and removed once.

---

## Space Complexity

```text
O(1)
```

### Reason

Only a few variables are used.

---

## What I Learned

- Difference between Fixed Size and Variable Size Sliding Window.
- How to initialize the first window.
- How to slide the window efficiently.
- Why we use:
  - `currentSum += nums[right]`
  - `currentSum -= nums[right-k]`
- How Sliding Window reduces the time complexity from **O(n × k)** to **O(n)**.

---

✅ Problem Solved: Maximum Average Subarray I (LeetCode #643)

🐍 Language: Python

📅 Day 43 of Daily DSA Practice
