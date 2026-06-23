# Day 25 of My DSA Journey 🚀

## Problem 25: Search Insert Position

### Difficulty
Easy

### Problem Link

[LeetCode - Search Insert Position](https://leetcode.com/problems/search-insert-position/)

### Problem Statement

Given a sorted array of distinct integers `nums` and a target value `target`, return the index if the target is found.

If not, return the index where it would be inserted in order.

You must write an algorithm with:

```text
O(log n)
```

runtime complexity.

---

## Optimized Approach (Binary Search)

- Use Binary Search on the sorted array.
- Find the middle element.
- If the target is found, return its index.
- If the target is smaller, search the left half.
- If the target is larger, search the right half.
- If the target is not found, return the position where it should be inserted.
- After Binary Search ends, `left` points to the correct insertion position.

---

## Example

### Input

```text
nums = [1,3,5,6]
target = 2
```

---

### Step 1

```text
left = 0
right = 3
```

Find middle:

```text
mid = (0 + 3) // 2 = 1
```

Middle element:

```text
nums[1] = 3
```

Compare:

```text
2 < 3
```

Move left:

```text
right = 0
```

---

### Step 2

```text
left = 0
right = 0
```

Find middle:

```text
mid = (0 + 0) // 2 = 0
```

Middle element:

```text
nums[0] = 1
```

Compare:

```text
2 > 1
```

Move right:

```text
left = 1
```

---

### Step 3

Now:

```text
left = 1
right = 0
```

Binary Search ends.

The insertion position is:

```text
left = 1
```

---

## Final Output

```text
1
```

---

## Explanation

The key idea is that when Binary Search fails to find the target, the `left` pointer automatically ends at the position where the target should be inserted.

This allows us to find both:

- The target index if it exists.
- The correct insertion position if it does not exist.

without performing any extra search.

---

## Time Complexity

```text
O(log n)
```

Reason:

- The search space is reduced by half in every iteration.

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
- How to find the insertion position of a target.
- Why `left` points to the correct insertion position.
- How to solve searching problems in O(log n) time.
- Why Binary Search requires a sorted array.

---

✅ Problem Solved: Search Insert Position (LeetCode #35)

🐍 Language: Python

📅 Day 25 of Daily DSA Practice
