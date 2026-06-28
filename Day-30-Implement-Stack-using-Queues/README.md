# Day 30 of My DSA Journey 🚀

## Problem 30: Implement Stack using Queues

### Difficulty
Easy

### Problem Link

[LeetCode - Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

### Problem Statement

Implement a Last-In-First-Out (LIFO) stack using queues.

The implemented stack should support the following operations:

- `push(x)` – Push element `x` onto the stack.
- `pop()` – Remove and return the top element.
- `top()` – Return the top element.
- `empty()` – Return `True` if the stack is empty; otherwise, return `False`.

---

## My Approach

- Create a stack using a Python list.
- Use `append()` to push elements.
- Use `pop()` to remove the top element.
- Access the last element using `[-1]` for the `top()` operation.
- Check whether the list is empty using its length.

---

## Example

### Operations

```text
push(1)
push(2)
top()
pop()
empty()
```

---

### Step 1

```text
Stack = [1]
```

---

### Step 2

```text
Stack = [1, 2]
```

---

### Step 3

```text
top()
```

Output

```text
2
```

---

### Step 4

```text
pop()
```

Output

```text
2
```

Stack becomes

```text
[1]
```

---

### Step 5

```text
empty()
```

Output

```text
False
```

---

## Explanation

The stack follows the **Last-In-First-Out (LIFO)** principle.

- `push()` adds an element to the end of the list.
- `pop()` removes the last element.
- `top()` returns the last element without removing it.
- `empty()` checks whether the stack contains any elements.

---

## Time Complexity

### push()

```text
O(1)
```

### pop()

```text
O(1)
```

### top()

```text
O(1)
```

### empty()

```text
O(1)
```

---

## Space Complexity

```text
O(n)
```

Reason:

- The stack stores all inserted elements.

---

## What I Learned

- How a Stack works.
- The LIFO (Last-In-First-Out) principle.
- How to implement stack operations in Python.
- How `append()`, `pop()`, and indexing can be used to build a stack.
- Time complexity of basic stack operations.

---

✅ Problem Solved: Implement Stack using Queues (LeetCode #225)

🐍 Language: Python

📅 Day 30 of Daily DSA Practice
