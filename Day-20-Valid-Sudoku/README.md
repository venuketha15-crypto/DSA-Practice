# Day 20 of My DSA Journey 🚀

## Problem 20: Valid Sudoku

### Difficulty
Medium

### Problem Link

[LeetCode - Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

### Problem Statement

Determine if a 9 × 9 Sudoku board is valid.

A valid Sudoku board must satisfy:

- Each row contains digits 1-9 without repetition.
- Each column contains digits 1-9 without repetition.
- Each 3 × 3 sub-box contains digits 1-9 without repetition.

Empty cells are represented by '.'.

---

## Optimized Approach (Hash Set)

- Create separate Hash Sets to track numbers seen in rows, columns, and 3×3 boxes.
- Traverse every cell of the Sudoku board.
- Skip empty cells represented by '.'.
- For each number:
  - Check whether it already exists in its row.
  - Check whether it already exists in its column.
  - Check whether it already exists in its 3×3 box.
- If a duplicate is found in any row, column, or box, return False.
- Otherwise, store the number in the corresponding row, column, and box sets.
- If all cells are processed without duplicates, return True.

---

## Example

### Input

```text
[
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
```

---

### Step 1: Visit Cell (0,0)

```text
Number = 5
```

Check:

```text
Row 0 → Does not contain 5
Column 0 → Does not contain 5
Box 0 → Does not contain 5
```

Store:

```text
Row 0 → {5}
Column 0 → {5}
Box 0 → {5}
```

---

### Step 2: Visit Cell (0,1)

```text
Number = 3
```

Check:

```text
Row 0 → Does not contain 3
Column 1 → Does not contain 3
Box 0 → Does not contain 3
```

Store:

```text
Row 0 → {5, 3}
Column 1 → {3}
Box 0 → {5, 3}
```

---

### Step 3: Continue Processing

Each number is checked against:

```text
Its Row
Its Column
Its 3×3 Box
```

If the number is unique, store it and continue.

---

### Duplicate Example

Suppose a row becomes:

```text
5 3 . . 7 . . . 5
```

When the last 5 is visited:

```text
Row 0 already contains 5
```

Therefore:

```text
Duplicate Found
```

Return:

```text
False
```

---

## Understanding the 3×3 Boxes

The Sudoku board contains 9 boxes:

```text
0 1 2
3 4 5
6 7 8
```

Examples:

```text
Cell (1,2) → Box 0
Cell (4,5) → Box 4
Cell (8,8) → Box 8
```

A box index helps identify which 3×3 box a cell belongs to.

---

## Final Output

```text
True
```

The board is valid because no duplicates exist in any row, column, or 3×3 box.

---

## Explanation

The key idea is to detect duplicates efficiently.

Hash Sets allow us to quickly determine whether a number has already appeared in:

```text
A Row
A Column
A 3×3 Box
```

Since Hash Sets provide O(1) lookup time, we can validate the Sudoku board efficiently.

---

## Time Complexity

```text
O(1)
```

Reason:

- Sudoku board size is fixed at 9 × 9.
- Only 81 cells are processed.

For a generalized n × n Sudoku:

```text
O(n²)
```

---

## Space Complexity

```text
O(1)
```

Reason:

- A fixed number of sets are used.
- Memory usage remains constant.

For a generalized n × n Sudoku:

```text
O(n²)
```

---

## What I Learned

- How Sudoku validation works.
- How to use Hash Sets for duplicate detection.
- How to validate rows efficiently.
- How to validate columns efficiently.
- How to validate 3×3 boxes efficiently.
- Why Hash Sets provide O(1) lookup.
- How box indexing helps identify the correct Sudoku box.
- Difference between brute force and optimized approaches.
- Why Hash Sets are preferred over Lists.

---

✅ Problem Solved: Valid Sudoku (LeetCode #36)

🐍 Language: Python

📅 Day 20 of Daily DSA Practice
