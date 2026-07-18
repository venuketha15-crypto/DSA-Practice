# Day 48 of My DSA Journey 🚀

## Problem 48: Rotate Image

### Difficulty
Medium

### Problem Link

[LeetCode - Rotate Image](https://leetcode.com/problems/rotate-image/)

---

## Problem Statement

You are given an `n × n` matrix representing an image.

Rotate the image by **90° clockwise** **in-place**.

> **In-place** means modifying the original matrix without creating another matrix.

---

## Optimized Approach (Transpose + Reverse)

The rotation can be performed in two simple steps:

1. **Transpose** the matrix.
2. **Reverse** every row.

This rotates the matrix **90° clockwise** without using any extra matrix.

---

## Example

### Input

```text
1 2 3
4 5 6
7 8 9
```

---

### Step 1: Transpose

Swap rows and columns.

```text
1 4 7
2 5 8
3 6 9
```

---

### Step 2: Reverse Every Row

Reverse each row individually.

```text
7 4 1
8 5 2
9 6 3
```

---

## Final Output

```text
7 4 1
8 5 2
9 6 3
```

---

## Explanation

The optimized solution avoids creating a new matrix.

- First, transpose the matrix by swapping `matrix[i][j]` with `matrix[j][i]`.
- Then, reverse every row.
- These two operations together rotate the matrix **90° clockwise**.

---

## Time Complexity

```text
O(n²)
```

### Reason

- Transposing visits each required element once.
- Reversing every row also visits each element once.

---

## Space Complexity

```text
O(1)
```

### Reason

The matrix is modified **in-place** without using an additional matrix.

---

## What I Learned

- What matrix rotation means.
- How transpose swaps rows and columns.
- Why reversing every row after transpose gives a 90° clockwise rotation.
- The difference between using an extra matrix (**O(n²)** space) and the in-place optimized approach (**O(1)** space).
- How to solve matrix rotation efficiently for coding interviews.

---

✅ Problem Solved: Rotate Image (LeetCode #48)

🐍 Language: Python

📅 Day 48 of Daily DSA Practice
