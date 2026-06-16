# Day 18 of My DSA Journey 🚀

## Problem 18: Product of Array Except Self

### Difficulty
Medium

### Problem Link

[LeetCode - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

### Problem Statement

Given an integer array `nums`, return an array `answer` such that:

```text
answer[i] is equal to the product of all the elements of nums except nums[i].
```

You must solve it **without using division** and in **O(n)** time complexity.

---

## Key Observation

For every index:

```text
Product Except Self
=
Product of all elements before it
×
Product of all elements after it
```

In other words:

```text
Answer[i]
=
Left Product × Right Product
```

Instead of recalculating these products for every index, we can reuse previously computed information.

---

## Prefix Product

Prefix means:

```text
Product of all elements BEFORE the current index.
```

For:

```text
nums = [1, 2, 3, 4]
```

Prefix products are:

| Index | Elements Before | Prefix Product |
|---------|------------------|-----------------|
| 0 | None | 1 |
| 1 | 1 | 1 |
| 2 | 1, 2 | 2 |
| 3 | 1, 2, 3 | 6 |

Prefix array:

```text
[1, 1, 2, 6]
```

---

## Suffix Product

Suffix means:

```text
Product of all elements AFTER the current index.
```

For:

```text
nums = [1, 2, 3, 4]
```

Suffix products are:

| Index | Elements After | Suffix Product |
|---------|-----------------|-----------------|
| 0 | 2, 3, 4 | 24 |
| 1 | 3, 4 | 12 |
| 2 | 4 | 4 |
| 3 | None | 1 |

Suffix array:

```text
[24, 12, 4, 1]
```

---

## Combining Prefix and Suffix

The answer for each index is:

```text
Prefix Product × Suffix Product
```

| Index | Prefix | Suffix | Answer |
|---------|---------|---------|----------|
| 0 | 1 | 24 | 24 |
| 1 | 1 | 12 | 12 |
| 2 | 2 | 4 | 8 |
| 3 | 6 | 1 | 6 |

Final Answer:

```text
[24, 12, 8, 6]
```

---

## Example

### Input

```text
nums = [1, 2, 3, 4]
```

### Output

```text
[24, 12, 8, 6]
```

### Explanation

For each index:

```text
answer[0] = 2 × 3 × 4 = 24

answer[1] = 1 × 3 × 4 = 12

answer[2] = 1 × 2 × 4 = 8

answer[3] = 1 × 2 × 3 = 6
```

---

## Why Prefix and Suffix Work

The brute-force approach recalculates the same products repeatedly.

For example:

```text
1 × 2
1 × 2 × 3
1 × 2
3 × 4
```

Many calculations are repeated.

Instead, Prefix remembers:

```text
Everything before me.
```

Suffix remembers:

```text
Everything after me.
```

By combining them, we avoid repeated work and solve the problem efficiently.

---

## Time Complexity

```text
O(n)
```

Reason:

- One pass to calculate Prefix Products.
- One pass to calculate Suffix Products.

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

Reason:

- Only constant extra space is used apart from the output array.

---

## What I Learned

- How to move from brute force thinking to optimized thinking.
- The Prefix Product technique.
- The Suffix Product technique.
- Why Product Except Self can be divided into left and right products.
- How to reuse previously computed information.
- Why storing current information before updating it is important.
- How to solve the problem in O(n) time without using division.
- How Prefix and Suffix patterns appear in many DSA problems.

---

✅ Problem Solved: Product of Array Except Self (LeetCode #238)

🐍 Language: Python

📅 Day 18 of Daily DSA Practice
