# Day 8 of My DSA Journey 🚀

## Problem 8: String to Integer (atoi)

### Difficulty
Medium

### Problem Link

[LeetCode - String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

### Problem Statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm should:

- Ignore leading whitespace.
- Check for an optional `+` or `-` sign.
- Read digits until a non-digit character is encountered.
- Clamp the result to the 32-bit signed integer range if it overflows.

### Approach

- Skip all leading spaces.
- Check whether the number is positive or negative.
- Traverse the string and process digit characters.
- Convert each digit and build the number using:

```python
num = num * 10 + digit
```

- Before updating the number, check whether adding the next digit would cause overflow.
- If overflow occurs, return:

```python
2147483647
```

for positive numbers or

```python
-2147483648
```

for negative numbers.

- Return the final result after applying the sign.

### Example

Input:

```text
s = "   -42"
```

Step 1:

Skip leading spaces:

```text
"   -42"
   ^
```

Move index until:

```text
"-42"
 ^
```

---

Step 2:

Check sign:

```python
sign = -1
```

Move to next character.

---

Step 3:

Read digit:

```python
digit = 4
```

Build number:

```python
num = 0 * 10 + 4
```

```text
num = 4
```

---

Step 4:

Read digit:

```python
digit = 2
```

Build number:

```python
num = 4 * 10 + 2
```

```text
num = 42
```

---

Step 5:

No more digits.

Apply sign:

```python
result = sign * num
```

```text
result = -42
```

Output:

```text
-42
```

### Explanation

The algorithm processes the string in three stages:

1. Skip leading spaces.
2. Determine the sign (`+` or `-`).
3. Read digits and build the number.

For:

```text
s = "   -42"
```

The digits are processed as:

```text
4 → 2
```

The number is built as:

```text
0 → 4 → 42
```

The sign is then applied:

```text
42 → -42
```

Before adding a new digit, the algorithm checks whether the value would exceed the 32-bit signed integer range.

This prevents integer overflow and ensures the correct result is returned.

### Time Complexity

O(n)

where n is the length of the string.

In the worst case, every character is visited once.

### Space Complexity

O(1)

Only a few variables are used regardless of input size.

### What I Learned

- How to skip leading whitespace in a string.
- How to handle positive and negative signs.
- How to convert characters into digits.
- How to build a number digit by digit.
- How to detect and handle integer overflow.
- How string parsing works in real-world applications.

✅ Problem Solved: String to Integer (atoi) (LeetCode #8)

🐍 Language: Python

📅 Day 8 of Daily DSA Practice
