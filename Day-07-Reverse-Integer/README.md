# Day 7 of My DSA Journey 🚀

## Problem 7: Reverse Integer

### Difficulty
Medium

### Problem Link

[LeetCode - Reverse Integer](https://leetcode.com/problems/reverse-integer/)

### Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, return `0`.

### Optimized Approach

- Store the sign of the number.
- Convert the number to its absolute value.
- Extract the last digit using `% 10`.
- Build the reversed number using:

```python
res = res * 10 + digit
```

- Remove the last digit using:

```python
x //= 10
```

- Restore the original sign.
- Check whether the result is within the 32-bit integer range.
- Return the result if valid, otherwise return `0`.

### Example

Input:

```text
x = 120
```

Initial:

```python
sign = 1
x = 120
res = 0
```

Step 1:

Extract last digit:

```python
digit = 120 % 10
```

```text
digit = 0
```

Build reversed number:

```python
res = 0 * 10 + 0
```

```text
res = 0
```

Remove last digit:

```python
x = 120 // 10
```

```text
x = 12
```

---

Step 2:

Extract last digit:

```python
digit = 12 % 10
```

```text
digit = 2
```

Build reversed number:

```python
res = 0 * 10 + 2
```

```text
res = 2
```

Remove last digit:

```python
x = 12 // 10
```

```text
x = 1
```

---

Step 3:

Extract last digit:

```python
digit = 1 % 10
```

```text
digit = 1
```

Build reversed number:

```python
res = 2 * 10 + 1
```

```text
res = 21
```

Remove last digit:

```python
x = 1 // 10
```

```text
x = 0
```

The loop ends because:

```python
while x
```

becomes false.

Restore sign:

```python
res *= sign
```

Final Output:

```text
21
```

### Explanation

The algorithm repeatedly extracts the last digit of the number and appends it to the result.

For:

```text
120
```

Digits are extracted in this order:

```text
0 → 2 → 1
```

The reversed number is built as:

```text
0 → 2 → 21
```

The sign is restored at the end using:

```python
res *= sign
```

Finally, the result is checked to ensure it lies within the signed 32-bit integer range.

Since `21` is within the valid range, it is returned.

### Time Complexity

O(log n)

where n is the value of the integer.

In each iteration, one digit is removed using:

```python
x //= 10
```

Therefore, the loop runs once for every digit in the number.

### Space Complexity

O(1)

Only a few variables are used.

### What I Learned

- How to extract digits using `% 10`.
- How to remove digits using `// 10`.
- How to reverse a number mathematically without converting it to a string.
- How to handle negative numbers using a sign variable.
- How to check for 32-bit integer overflow.

✅ Problem Solved: Reverse Integer (LeetCode #7)

🐍 Language: Python

📅 Day 7 of Daily DSA Practice
