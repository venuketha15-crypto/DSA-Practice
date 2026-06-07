# Day 9 of My DSA Journey 🚀

## Problem 9: Palindrome Number

### Difficulty
Easy

### Problem Link

[LeetCode - Palindrome Number](https://leetcode.com/problems/palindrome-number/)

### Problem Statement

Given an integer `x`, return `true` if `x` is a palindrome and `false` otherwise.

A palindrome number reads the same forward and backward.

### Approach

- Negative numbers cannot be palindromes because of the negative sign.
- Store the original number in a temporary variable.
- Reverse the number digit by digit.
- Compare the reversed number with the original number.
- If both are equal, the number is a palindrome.

### Example

Input:

```text
x = 121
```

Initial:

```python
rev = 0
temp = 121
```

Step 1:

Extract last digit:

```python
digit = 121 % 10
```

```text
digit = 1
```

Build reversed number:

```python
rev = 0 * 10 + 1
```

```text
rev = 1
```

Remove last digit:

```python
temp = 121 // 10
```

```text
temp = 12
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
rev = 1 * 10 + 2
```

```text
rev = 12
```

Remove last digit:

```python
temp = 12 // 10
```

```text
temp = 1
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
rev = 12 * 10 + 1
```

```text
rev = 121
```

Remove last digit:

```python
temp = 1 // 10
```

```text
temp = 0
```

The loop ends because:

```python
while temp
```

becomes false.

Final Comparison:

```python
rev == x
```

```text
121 == 121
```

Output:

```text
True
```

### Explanation

The algorithm reverses the given number and compares it with the original number.

For:

```text
121
```

Digits are extracted in this order:

```text
1 → 2 → 1
```

The reversed number is built as:

```text
0 → 1 → 12 → 121
```

Since the reversed number is equal to the original number, the number is a palindrome.

For a negative number such as:

```text
-121
```

the algorithm immediately returns:

```text
False
```

because negative numbers cannot be palindromes.

### Time Complexity

O(log n)

where n is the value of the integer.

In each iteration, one digit is removed using:

```python
temp //= 10
```

Therefore, the loop runs once for every digit in the number.

### Space Complexity

O(1)

Only a few variables are used.

### What I Learned

- How to reverse a number mathematically.
- How to extract digits using `% 10`.
- How to remove digits using `// 10`.
- How to compare a reversed number with the original number.
- Why negative numbers cannot be palindromes.
- How to solve palindrome-related problems without converting numbers to strings.

✅ Problem Solved: Palindrome Number (LeetCode #9)

🐍 Language: Python

📅 Day 9 of Daily DSA Practice
