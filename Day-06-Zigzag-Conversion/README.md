# Day 6 of My DSA Journey 🚀

## Problem 6: Zigzag Conversion

### Difficulty
Medium

### Problem Link

[LeetCode - Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/)

### Problem Statement

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows.

After writing the characters in a zigzag pattern, read the rows one by one and return the resulting string.

### Optimized Approach

- Create a list of strings, one for each row.
- Traverse the input string character by character.
- Add each character to the current row.
- Move downward through the rows.
- When the last row is reached, change direction and move upward.
- When the first row is reached, change direction and move downward again.
- Finally, join all rows to get the result.

### Example

Input:

s = "PAYPALISHIRING"

numRows = 3

Initial:

```python
rows = ["", "", ""]
row = 0
step = 1
```

Step 1:

Character = P

```python
rows[0] += "P"
```

Rows:

```text
Row 0: P
Row 1:
Row 2:
```

Since:

```python
row == 0
```

Direction remains:

```python
step = 1
```

Move:

```python
row += step
```

row = 1

---

Step 2:

Character = A

```python
rows[1] += "A"
```

Rows:

```text
Row 0: P
Row 1: A
Row 2:
```

Move:

```python
row = 2
```

---

Step 3:

Character = Y

```python
rows[2] += "Y"
```

Rows:

```text
Row 0: P
Row 1: A
Row 2: Y
```

Since:

```python
row == numRows - 1
```

Change direction:

```python
step = -1
```

Move:

```python
row = 1
```

---

Step 4:

Character = P

```python
rows[1] += "P"
```

Rows:

```text
Row 0: P
Row 1: AP
Row 2: Y
```

Move:

```python
row = 0
```

---

Step 5:

Character = A

```python
rows[0] += "A"
```

Rows:

```text
Row 0: PA
Row 1: AP
Row 2: Y
```

Since:

```python
row == 0
```

Change direction:

```python
step = 1
```

The process continues until all characters are placed.

Final Rows:

```text
Row 0: PAHN
Row 1: APLSIIG
Row 2: YIR
```

Output:

```text
PAHNAPLSIIGYIR
```

### Explanation

The algorithm uses:

```python
row
```

to track the current row and

```python
step
```

to track the direction.

When the first row is reached:

```python
row == 0
```

the direction becomes:

```python
step = 1
```

which moves downward.

When the last row is reached:

```python
row == numRows - 1
```

the direction becomes:

```python
step = -1
```

which moves upward.

This continuous change of direction creates the zigzag pattern.

Finally, all rows are joined together using:

```python
"".join(rows)
```

to produce the final answer.

### Time Complexity

O(n)

where n is the length of the string.

Each character is processed exactly once.

### Space Complexity

O(n)

The rows list stores all characters of the input string.

### What I Learned

- How to simulate movement between rows.
- How to change direction dynamically.
- How to use a list of strings efficiently.
- How zigzag traversal works.
- How to solve the problem without creating a full matrix.

✅ Problem Solved: Zigzag Conversion (LeetCode #6)

🐍 Language: Python

📅 Day 6 of Daily DSA Practice
