# Day 39 of My DSA Journey 🚀

## Problem 39: Decode String

### Difficulty
Medium

### Problem Link

[LeetCode - Decode String](https://leetcode.com/problems/decode-string/)

### Problem Statement

Given an encoded string, decode it according to the following rule:

```text
k[encoded_string]
```

This means the `encoded_string` inside the brackets should be repeated **k** times.

Return the decoded string.

---

## Optimized Approach (Stack)

- Create an empty stack.
- Traverse each character in the string.
- Push every character onto the stack until a closing bracket `]` is found.
- When `]` is found:
  - Pop characters until `[` to get the encoded string.
  - Remove the `[` from the stack.
  - Pop the digits before `[` to get the repeat count.
  - Repeat the string `count` times.
  - Push the decoded string back onto the stack.
- Finally, join all elements in the stack to get the answer.

---

## Example

### Input

```text
s = "3[a2[c]]"
```

---

### Step 1

Read characters until the first `]`

```text
Stack = ['3','[','a','2','[','c']
```

---

### Step 2

Found `]`

```text
String = "c"
Number = 2
```

Repeat:

```text
2 × "c" = "cc"
```

Push back:

```text
Stack = ['3','[','a','cc']
```

---

### Step 3

Continue until the next `]`

```text
String = "acc"
Number = 3
```

Repeat:

```text
3 × "acc" = "accaccacc"
```

Push back:

```text
Stack = ["accaccacc"]
```

---

## Final Output

```text
"accaccacc"
```

---

## Explanation

The stack stores the processed characters.

Whenever a closing bracket `]` is found:

- Extract the encoded string.
- Extract the repeat count.
- Repeat the string.
- Push the decoded result back onto the stack.

This allows nested encoded strings to be decoded from the inside out.

---

## Time Complexity

```text
O(n)
```

### Reason

- Every character is pushed into the stack at most once.
- Every character is popped from the stack at most once.

---

## Space Complexity

```text
O(n)
```

### Reason

The stack stores the characters and partially decoded strings.

---

## What I Learned

- How to decode nested strings using a stack.
- How to extract numbers and strings separately.
- How to use string multiplication (`count * string`) in Python.
- Why stacks are useful for nested bracket problems.
- Why the optimized solution runs in **O(n)** time.

---

✅ Problem Solved: Decode String (LeetCode #394)

🐍 Language: Python

📅 Day 39 of Daily DSA Practice
```
