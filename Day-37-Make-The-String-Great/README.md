# Day 37 of My DSA Journey 🚀

## Problem 37: Make The String Great

### Difficulty
Easy

### Problem Link

[LeetCode - Make The String Great](https://leetcode.com/problems/make-the-string-great/)

### Problem Statement

A string is considered **good** if it does not contain two adjacent characters that are the same letter but in different cases.

For example:

- `'a'` and `'A'`
- `'B'` and `'b'`

If such a pair exists, remove both characters.

Continue this process until the string becomes good.

Return the final string.

---

## Optimized Approach (Stack)

- Create an empty stack.
- Traverse each character in the string.
- Compare the current character with the top of the stack.
- If the ASCII difference between them is `32`, they are the same letter in different cases, so remove the top element.
- Otherwise, push the current character onto the stack.
- Join the remaining characters in the stack to get the final string.

---

## Example

### Input

```text
s = "leEeetcode"
```

---

### Step 1

Read `'l'`

```text
Stack = [l]
```

---

### Step 2

Read `'e'`

```text
Stack = [l, e]
```

---

### Step 3

Read `'E'`

ASCII Difference:

```text
abs(ord('e') - ord('E')) = 32
```

Remove `'e'`

```text
Stack = [l]
```

---

### Step 4

Read `'e'`

```text
Stack = [l, e]
```

---

### Continue

Process the remaining characters.

Final Stack:

```text
[l, e, e, t, c, o, d, e]
```

---

## Final Output

```text
"leetcode"
```

---

## Explanation

The stack stores the processed characters.

- If the current character and the top of the stack are the same letter with different cases, remove the top character.
- Otherwise, push the current character.
- Continue until the entire string is processed.

The remaining characters form the final good string.

---

## Time Complexity

```text
O(n)
```

### Reason

Each character is pushed into the stack at most once and popped at most once.

---

## Space Complexity

```text
O(n)
```

### Reason

In the worst case, all characters remain in the stack.

---

## What I Learned

- How to use a stack for string processing.
- How ASCII values help compare uppercase and lowercase letters.
- Why `abs(ord(a) - ord(b)) == 32` identifies the same letter with different cases.
- How `append()` and `pop()` make the solution efficient.
- Why the optimized solution runs in **O(n)** time.

---

✅ Problem Solved: Make The String Great (LeetCode #1544)

🐍 Language: Python

📅 Day 37 of Daily DSA Practice
```
