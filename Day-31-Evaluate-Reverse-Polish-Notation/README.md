# Day 31 of My DSA Journey 🚀

## Problem 31: Evaluate Reverse Polish Notation

### Difficulty
Medium

### Problem Link

[LeetCode - Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

### Problem Statement

You are given an array of strings `tokens` representing an arithmetic expression in Reverse Polish Notation (RPN).

Evaluate the expression and return its value.

The valid operators are:

- `+`
- `-`
- `*`
- `/`

Division should truncate toward zero.

---

## Optimized Approach (Stack)

- Create an empty stack.
- Traverse each token from left to right.
- If the token is a number, push it onto the stack.
- If the token is an operator, pop the top two numbers from the stack.
- Perform the operation based on the operator.
- Push the result back onto the stack.
- After processing all tokens, the remaining element in the stack is the final answer.

---

## Example

### Input

```text
tokens = ["2","1","+","3","*"]
```

---

### Step 1

Read:

```text
2
```

Stack:

```text
[2]
```

---

### Step 2

Read:

```text
1
```

Stack:

```text
[2, 1]
```

---

### Step 3

Read:

```text
+
```

Pop:

```text
2 and 1
```

Calculate:

```text
2 + 1 = 3
```

Push result:

```text
[3]
```

---

### Step 4

Read:

```text
3
```

Stack:

```text
[3, 3]
```

---

### Step 5

Read:

```text
*
```

Pop:

```text
3 and 3
```

Calculate:

```text
3 × 3 = 9
```

Push result:

```text
[9]
```

---

## Final Output

```text
9
```

---

## Explanation

The stack follows the **Last-In-First-Out (LIFO)** principle.

- Numbers are pushed onto the stack.
- When an operator is found, the top two numbers are removed.
- The operation is performed.
- The result is pushed back onto the stack.
- After all tokens are processed, the only remaining value is the final answer.

---

## Time Complexity

```text
O(n)
```

Reason:

- Each token is processed exactly once.
- Every push and pop operation takes O(1).

---

## Space Complexity

```text
O(n)
```

Reason:

- In the worst case, the stack stores all numbers before processing the operators.

---

## What I Learned

- How to solve expression evaluation problems using a Stack.
- How Reverse Polish Notation (RPN) works.
- Why the order of operands matters for subtraction and division.
- How to use push and pop operations effectively.
- Why the solution runs in O(n) time complexity.

---

✅ Problem Solved: Evaluate Reverse Polish Notation (LeetCode #150)

🐍 Language: Python

📅 Day 31 of Daily DSA Practice
```
