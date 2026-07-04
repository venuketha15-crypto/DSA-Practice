# Day 36 of My DSA Journey 🚀

## Problem 36: Remove All Adjacent Duplicates in String

### Difficulty
Easy

### Problem Link

[LeetCode - Remove All Adjacent Duplicates in String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

### Problem Statement

Given a string `s`, repeatedly remove adjacent duplicate characters until no duplicate pairs remain.

Return the final string.

---

## Optimized Approach (Stack)

- Create an empty stack.
- Traverse each character in the string.
- If the stack is not empty and the current character matches the top of the stack, remove the top character using `pop()`.
- Otherwise, push the current character onto the stack.
- Finally, join all characters in the stack to form the answer.

---

## Example

### Input

```text
s = "abbaca"
```

---

### Step 1

Read `'a'`

```text
Stack = [a]
```

---

### Step 2

Read `'b'`

```text
Stack = [a, b]
```

---

### Step 3

Read another `'b'`

Top of stack is also `'b'`.

```text
Pop 'b'

Stack = [a]
```

---

### Step 4

Read `'a'`

Top of stack is also `'a'`.

```text
Pop 'a'

Stack = []
```

---

### Step 5

Read `'c'`

```text
Stack = [c]
```

---

### Step 6

Read `'a'`

```text
Stack = [c, a]
```

---

## Final Output

```text
"ca"
```

---

## Explanation

The stack stores the characters processed so far.

- If the current character is different from the top of the stack, push it.
- If it is the same, remove the top element.
- Continue until the entire string is processed.
- The remaining characters in the stack form the final answer.

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

In the worst case, all characters are stored in the stack.

---

## What I Learned

- How to use a stack to process strings.
- How `append()` and `pop()` simplify adjacent duplicate removal.
- Why checking the top of the stack is enough.
- How to convert a stack back into a string using `"".join(stack)`.
- Why the optimized solution runs in **O(n)** time.

---

✅ Problem Solved: Remove All Adjacent Duplicates in String (LeetCode #1047)

🐍 Language: Python

📅 Day 36 of Daily DSA Practice
```
