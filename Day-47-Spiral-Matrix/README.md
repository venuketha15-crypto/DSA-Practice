# Day 47 of My DSA Journey 🚀

## Problem 47: Spiral Matrix

### Difficulty
Medium

### Problem Link

[LeetCode - Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

---

## Problem Statement

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

---

## Optimized Approach (Boundary Traversal)

- Maintain four boundaries:
  - `top`
  - `bottom`
  - `left`
  - `right`
- Traverse the matrix layer by layer.
- Follow the order:
  1. Left → Right (Top Row)
  2. Top → Bottom (Right Column)
  3. Right → Left (Bottom Row)
  4. Bottom → Top (Left Column)
- After each traversal, shrink the corresponding boundary.
- Continue until all elements are visited.

---

## Example

### Input

```text
1 2 3
4 5 6
7 8 9
```

---

### Step 1: Traverse Top Row

```text
1 → 2 → 3
```

Result:

```text
[1,2,3]
```

Update:

```text
top = 1
```

---

### Step 2: Traverse Right Column

```text
6
↓
9
```

Result:

```text
[1,2,3,6,9]
```

Update:

```text
right = 1
```

---

### Step 3: Traverse Bottom Row

```text
8 ← 7
```

Result:

```text
[1,2,3,6,9,8,7]
```

Update:

```text
bottom = 1
```

---

### Step 4: Traverse Left Column

```text
4
```

Result:

```text
[1,2,3,6,9,8,7,4]
```

Update:

```text
left = 1
```

---

### Step 5: Remaining Matrix

```text
5
```

Traverse it.

Final Result:

```text
[1,2,3,6,9,8,7,4,5]
```

---

## Explanation

The algorithm treats the matrix like layers of an onion.

- Traverse the outer boundary.
- Shrink the boundaries.
- Repeat the same process for the remaining inner matrix.
- Stop when all elements have been visited.

---

## Time Complexity

```text
O(m × n)
```

### Reason

Each element in the matrix is visited exactly once.

---

## Space Complexity

```text
O(1)
```

### Reason

Only four boundary variables (`top`, `bottom`, `left`, `right`) are used.

> **Note:** The returned list stores all elements, so if output space is counted, the total space becomes **O(m × n)**.

---

## What I Learned

- What a matrix traversal is.
- How to use four boundaries (`top`, `bottom`, `left`, `right`).
- Why the traversal order is:
  - Top Row
  - Right Column
  - Bottom Row
  - Left Column
- Why we update each boundary after traversing it.
- Why a `while` loop is necessary to process every layer of the matrix.
- How to solve Spiral Matrix in **O(m × n)** time.

---

✅ Problem Solved: Spiral Matrix (LeetCode #54)

🐍 Language: Python

📅 Day 47 of Daily DSA Practice
