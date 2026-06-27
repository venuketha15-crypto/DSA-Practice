# Day 29 of My DSA Journey 🚀

## Problem 29: Min Stack

### Difficulty
Medium

### Problem Link

[LeetCode - Min Stack](https://leetcode.com/problems/min-stack/)

### Problem Statement

Design a stack that supports the following operations in constant time:

- `push(val)` – Push an element onto the stack.
- `pop()` – Remove the top element from the stack.
- `top()` – Return the top element.
- `getMin()` – Retrieve the minimum element in the stack.

All operations must run in:

```text
O(1)
```

time complexity.

---

## Optimized Approach (Two Stacks)

- Use one stack to store all elements.
- Use another stack to keep track of the minimum elements.
- Whenever a new element is smaller than or equal to the current minimum, push it into the minimum stack.
- When removing an element, remove it from the minimum stack as well if it is the current minimum.
- The top of the minimum stack always stores the minimum element.

---

## Example

### Operations

```text
push(-2)
push(0)
push(-3)
```

Main Stack

```text
[-2, 0, -3]
```

Min Stack

```text
[-2, -3]
```

---

### Operation

```text
getMin()
```

Output

```text
-3
```

---

### Operation

```text
pop()
```

Main Stack

```text
[-2, 0]
```

Min Stack

```text
[-2]
```

---

### Operation

```text
top()
```

Output

```text
0
```

---

### Operation

```text
getMin()
```

Output

```text
-2
```

---

## Explanation

The main stack stores all the elements.

The minimum stack stores only the minimum values encountered so far.

Whenever a new minimum value is pushed, it is also pushed into the minimum stack.

When the current minimum is removed, it is removed from both stacks.

This allows retrieving the minimum element in constant time.

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

### getMin()

```text
O(1)
```

---

## Space Complexity

```text
O(n)
```

Reason:

- Two stacks are used to store the elements and minimum values.

---

## What I Learned

- How a Stack works.
- How to maintain the minimum element efficiently.
- Why using two stacks makes `getMin()` run in O(1).
- How to design a data structure with constant-time operations.
- Difference between a normal stack and a Min Stack.

---

✅ Problem Solved: Min Stack (LeetCode #155)

🐍 Language: Python

📅 Day 29 of Daily DSA Practice
