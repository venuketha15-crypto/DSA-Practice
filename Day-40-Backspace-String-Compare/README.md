# Day 40 of My DSA Journey 🚀

## Problem 40: Backspace String Compare

### Difficulty
Easy

### Problem Link

[LeetCode - Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

### Problem Statement

Given two strings `s` and `t`, where `'#'` represents a backspace character, return `True` if the two strings are equal after applying all backspace operations. Otherwise, return `False`.

---

## Optimized Approach (Stack)

- Create a stack for each string.
- Traverse each character.
- If the character is not `'#'`, push it onto the stack.
- If the character is `'#'` and the stack is not empty, remove the last character using `pop()`.
- Repeat the same process for both strings.
- Finally, compare the two stacks.

---

## Example

### Input

```text
s = "ab#c"
t = "ad#c"
```

---

### Processing `s`

```text
Read 'a' → [a]

Read 'b' → [a, b]

Read '#' → [a]

Read 'c' → [a, c]
```

Final Stack:

```text
[a, c]
```

---

### Processing `t`

```text
Read 'a' → [a]

Read 'd' → [a, d]

Read '#' → [a]

Read 'c' → [a, c]
```

Final Stack:

```text
[a, c]
```

---

## Final Output

```text
True
```

Both processed strings are equal.

---

## Explanation

The stack simulates typing in a text editor.

- Normal characters are added to the stack.
- `'#'` removes the most recently added character if one exists.
- After processing both strings, compare the resulting stacks.

---

## Time Complexity

```text
O(n + m)
```

### Reason

- Each character in both strings is processed exactly once.

---

## Space Complexity

```text
O(n + m)
```

### Reason

- In the worst case, all characters from both strings are stored in their respective stacks.

---

## What I Learned

- How to simulate backspace operations using a stack.
- Why `append()` and `pop()` are useful for text editing problems.
- How to compare the final processed strings efficiently.
- Why checking if the stack is empty before calling `pop()` is important.
- Why the stack solution runs in **O(n + m)** time.

---

✅ Problem Solved: Backspace String Compare (LeetCode #844)

🐍 Language: Python

📅 Day 40 of Daily DSA Practice
```
