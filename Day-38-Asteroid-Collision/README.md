# Day 38 of My DSA Journey 🚀

## Problem 38: Asteroid Collision

### Difficulty
Medium

### Problem Link

[LeetCode - Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

### Problem Statement

You are given an integer array `asteroids`.

- A positive value represents an asteroid moving to the **right**.
- A negative value represents an asteroid moving to the **left**.
- The absolute value represents the asteroid's size.

When two asteroids moving in opposite directions collide:

- The smaller asteroid explodes.
- If both are the same size, both explode.
- Asteroids moving in the same direction never collide.

Return the state of the asteroids after all collisions.

---

## Optimized Approach (Stack)

- Create an empty stack.
- Traverse each asteroid.
- If there is no possible collision, push the asteroid onto the stack.
- If a collision occurs:
  - Remove the smaller asteroid.
  - If both are the same size, remove both.
  - If the current asteroid survives, continue checking for more collisions.
- Finally, return the remaining asteroids in the stack.

---

## Example

### Input

```text
asteroids = [10,2,-5]
```

---

### Step 1

Read `10`

```text
Stack = [10]
```

---

### Step 2

Read `2`

```text
Stack = [10,2]
```

---

### Step 3

Read `-5`

Collision:

```text
2 vs -5
```

Since

```text
5 > 2
```

`2` explodes.

```text
Stack = [10]
```

---

### Step 4

`-5` is still moving.

Another collision:

```text
10 vs -5
```

Since

```text
10 > 5
```

`-5` explodes.

```text
Stack = [10]
```

---

## Final Output

```text
[10]
```

---

## Explanation

The stack stores the asteroids that have survived so far.

Whenever a left-moving asteroid meets a right-moving asteroid:

- The smaller asteroid is destroyed.
- If both have the same size, both are destroyed.
- If the current asteroid survives, it continues colliding with earlier asteroids.

This process continues until there are no more collisions.

---

## Time Complexity

```text
O(n)
```

### Reason

- Every asteroid is pushed into the stack at most once.
- Every asteroid is popped from the stack at most once.
- Therefore, the total number of operations is linear.

---

## Space Complexity

```text
O(n)
```

### Reason

In the worst case, no collisions occur, so all asteroids remain in the stack.

---

## What I Learned

- How to simulate collisions using a stack.
- Why only asteroids moving in opposite directions can collide.
- How `while` handles multiple collisions efficiently.
- Why each asteroid is pushed and popped at most once.
- Why a `for` loop with a `while` loop can still have **O(n)** time complexity.

---

✅ Problem Solved: Asteroid Collision (LeetCode #735)

🐍 Language: Python

📅 Day 38 of Daily DSA Practice
```
