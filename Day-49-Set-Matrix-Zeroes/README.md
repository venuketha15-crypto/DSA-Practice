# Day 49 of My DSA Journey 🚀

## Problem 49: Set Matrix Zeroes

### Difficulty
Medium

### Problem Link

[LeetCode - Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

---

## Problem Statement

You are given an `m × n` matrix.

If any element in the matrix is `0`, set its **entire row** and **entire column** to `0`.

The matrix must be modified **in-place**.

> **In-place** means modifying the original matrix without creating another matrix for the result.

---

## Optimized Approach (First Row + First Column as Markers)

Instead of using extra arrays to remember which rows and columns should become `0`, we use the matrix itself.

1. Check whether the **first row** originally contains a `0`.
2. Check whether the **first column** originally contains a `0`.
3. Use the **first column** to mark which rows should become `0`.
4. Use the **first row** to mark which columns should become `0`.
5. Use these markers to update the remaining cells.
6. Finally, update the first row and first column if required.

This allows us to solve the problem using **O(1) extra space**.

---

## Example

### Input

```text
1 1 1
1 0 1
1 1 1
```

There is a `0` at:

```text
Row 1, Column 1
```

So:

- Row 1 must become `0`.
- Column 1 must become `0`.

---

### Step 1: Create Markers

Since the `0` is at Row 1, Column 1:

- Mark the beginning of Row 1 as `0`.
- Mark the top of Column 1 as `0`.

The matrix temporarily becomes:

```text
1 0 1
0 0 1
1 1 1
```

Here:

- The `0` in the first column tells us that **Row 1** must become zero.
- The `0` in the first row tells us that **Column 1** must become zero.

---

### Step 2: Use the Markers

Using those markers, make the required row and column zero.

```text
1 0 1
0 0 0
1 0 1
```

---

## Final Output

```text
1 0 1
0 0 0
1 0 1
```

---

## Explanation

The optimized solution avoids using separate arrays for storing rows and columns.

- The **first column** is used to remember which rows need to become `0`.
- The **first row** is used to remember which columns need to become `0`.
- We separately remember whether the first row and first column originally contained a `0`.
- After creating all the markers, we use them to update the matrix.
- Finally, we update the first row and first column if they originally contained a zero.

We should not immediately make an entire row and column zero when we find a `0`, because the newly created zeroes could incorrectly affect other rows and columns.

---

## Time Complexity

```text
O(m × n)
```

### Reason

We traverse the matrix to find zeroes, create markers, and update the required cells.

Each cell is processed only a constant number of times.

---

## Space Complexity

```text
O(1)
```

### Reason

No extra row or column arrays are used.

The **first row and first column of the matrix itself** are used as markers.

---

## What I Learned

- How to set an entire row and column to zero when a zero is found.
- Why we should not modify rows and columns immediately while finding zeroes.
- How the first row and first column can be used as markers.
- Why the original state of the first row and first column must be stored separately.
- How to improve the extra space from **O(m + n)** to **O(1)**.
- How to reuse part of the input matrix as temporary storage.

---

✅ Problem Solved: Set Matrix Zeroes (LeetCode #73)

🐍 Language: Python

📅 Day 49 of Daily DSA Practice
