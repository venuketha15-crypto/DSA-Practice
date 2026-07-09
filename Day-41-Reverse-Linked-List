# Day 41 of My DSA Journey 🚀

## Problem 41: Reverse Linked List

### Difficulty
Easy

### Problem Link

[LeetCode - Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

---

## Problem Statement

Given the `head` of a singly linked list, reverse the linked list and return the new head.

---

## Optimized Approach (Three Pointers)

- Use three pointers:
  - `prev`
  - `curr`
  - `nextNode`
- Traverse the linked list once.
- Save the next node before changing any links.
- Reverse the current node's pointer.
- Move all pointers one step forward.
- Continue until the end of the list.
- Return `prev`, which becomes the new head of the reversed list.

---

## Example

### Input

```text
1 → 2 → 3 → 4 → 5 → None
```

---

### Initial State

```text
prev = None
curr = 1
```

---

### Iteration 1

```text
nextNode = 2

1 → None

prev = 1
curr = 2
```

---

### Iteration 2

```text
nextNode = 3

2 → 1 → None

prev = 2
curr = 3
```

---

### Iteration 3

```text
nextNode = 4

3 → 2 → 1 → None

prev = 3
curr = 4
```

---

### Iteration 4

```text
nextNode = 5

4 → 3 → 2 → 1 → None

prev = 4
curr = 5
```

---

### Iteration 5

```text
nextNode = None

5 → 4 → 3 → 2 → 1 → None

prev = 5
curr = None
```

---

## Final Output

```text
5 → 4 → 3 → 2 → 1 → None
```

---

## Explanation

The key step is:

```python
curr.next = prev
```

This reverses the direction of the current node's pointer.

Before:

```text
1 → 2
```

After:

```text
1 ← 2
```

Repeating this for every node reverses the entire linked list.

---

## Time Complexity

```text
O(n)
```

### Reason

Each node is visited exactly once.

---

## Space Complexity

```text
O(1)
```

### Reason

Only three pointers (`prev`, `curr`, and `nextNode`) are used. No extra data structures are required.

---

## What I Learned

- How a singly linked list stores data using nodes.
- The role of `head`, `next`, and pointers.
- Why we need `prev`, `curr`, and `nextNode`.
- How changing `curr.next = prev` reverses a link.
- Why the iterative solution works in **O(n)** time and **O(1)** space.

---

✅ Problem Solved: Reverse Linked List (LeetCode #206)

🐍 Language: Python

📅 Day 41 of Daily DSA Practice
