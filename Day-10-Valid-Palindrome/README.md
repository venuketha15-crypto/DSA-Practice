# Day 10 of My DSA Journey 🚀

## Problem 10: Valid Palindrome

### Difficulty
Easy

### Problem Link

[LeetCode - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

### Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Brute Force Approach

- Traverse the string and keep only alphanumeric characters.
- Convert all characters to lowercase.
- Store the cleaned characters in a list.
- Join the list to form a string.
- Reverse the string.
- Compare the cleaned string with its reversed version.
- If both are equal, return `True`; otherwise return `False`.

### Time Complexity of Brute Force

O(n)

where n is the length of the string.

We traverse the string once to create the cleaned list, join it into a string, and reverse it.

### Space Complexity of Brute Force

O(n)

Extra space is used for:

- The list storing cleaned characters.
- The cleaned string.
- The reversed string.

### Optimized Approach (Two Pointers)

- Use two pointers: `left` and `right`.
- Start `left` from the beginning of the string and `right` from the end.
- Skip all non-alphanumeric characters using `isalnum()`.
- Convert characters to lowercase before comparison.
- If the characters do not match, return `False`.
- Move both pointers toward the center.
- If all characters match, return `True`.

### Example

Input:

```text
s = "A man, a plan, a canal: Panama"
```

Initial:

```python
left = 0
right = len(s) - 1
```

Step 1:

Compare:

```text
A == a
```

After converting to lowercase:

```text
a == a
```

Move pointers inward.

---

Step 2:

Skip spaces and commas.

Compare:

```text
m == m
```

Move pointers inward.

---

Step 3:

Compare:

```text
a == a
```

Move pointers inward.

---

Continue the same process while skipping non-alphanumeric characters.

Characters compared:

```text
a == a
m == m
a == a
n == n
...
```

All characters match.

Output:

```text
True
```

### Explanation

The Two Pointers approach compares characters from both ends of the string.

For:

```text
"A man, a plan, a canal: Panama"
```

Non-alphanumeric characters such as:

```text
' '
','
':'
```

are ignored.

The remaining characters become:

```text
amanaplanacanalpanama
```

Reading from left to right and right to left gives the same result.

Therefore:

```text
True
```

is returned.

The optimized solution avoids creating a new string and uses constant extra space.

### Time Complexity

O(n)

where n is the length of the string.

Each character is visited at most once by the two pointers.

### Space Complexity

O(1)

No extra data structure is used.

### What I Learned

- How to solve palindrome problems using the Two Pointers technique.
- How to skip unwanted characters using `isalnum()`.
- How to compare characters case-insensitively using `lower()`.
- The difference between a brute-force solution and an optimized solution.
- How to reduce space complexity from O(n) to O(1).
- Why Two Pointers is a common and efficient interview pattern.

✅ Problem Solved: Valid Palindrome (LeetCode #125)

🐍 Language: Python

📅 Day 10 of Daily DSA Practice
