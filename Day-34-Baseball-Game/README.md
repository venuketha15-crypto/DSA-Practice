# Day 34 of My DSA Journey 🚀

## Problem 34: Baseball Game

### Difficulty
Easy

### Problem Link

[LeetCode - Baseball Game](https://leetcode.com/problems/baseball-game/)

### Problem Statement

You are given a list of operations representing scores in a baseball game.

Each operation can be:

- An integer → Record a new score.
- `"+"` → Record the sum of the previous two scores.
- `"D"` → Record double the previous score.
- `"C"` → Remove the previous score.

Return the total score after performing all the operations.

---

## Optimized Approach (Stack)

- Create an empty stack.
- Traverse each operation one by one.
- If the operation is a number, push it into the stack.
- If the operation is `"+"`, add the last two scores and push the result.
- If the operation is `"D"`, double the last score and push the result.
- If the operation is `"C"`, remove the last score using `pop()`.
- Finally, return the sum of all values in the stack.

---

## Example

### Input

```text
operations = ["5","2","C","D","+"]
```

---

### Step 1

Operation:

```text
5
```

Stack:

```text
[5]
```

---

### Step 2

Operation:

```text
2
```

Stack:

```text
[5,2]
```

---

### Step 3

Operation:

```text
C
```

Remove the previous score.

Stack:

```text
[5]
```

---

### Step 4

Operation:

```text
D
```

Double the last score.

```text
5 × 2 = 10
```

Stack:

```text
[5,10]
```

---

### Step 5

Operation:

```text
+
```

Add the last two scores.

```text
5 + 10 = 15
```

Stack:

```text
[5,10,15]
```

---

## Final Output

```text
30
```

---

## Explanation

The stack stores all valid scores.

- Numbers are pushed into the stack.
- `"+"` uses the previous two scores.
- `"D"` doubles the previous score.
- `"C"` removes the last score.

At the end, adding all elements in the stack gives the final score.

---

## Time Complexity

```text
O(n)
```

### Reason

- Each operation is processed exactly once.
- Stack operations (`append()` and `pop()`) take **O(1)** time.

---

## Space Complexity

```text
O(n)
```

### Reason

- In the worst case, all valid scores are stored in the stack.

---

## What I Learned

- How to simulate operations using a Stack.
- How `append()` and `pop()` help manage the stack efficiently.
- How to access the top elements using `stack[-1]` and `stack[-2]`.
- How different stack operations can solve real-world simulation problems.
- Why the optimized solution runs in **O(n)** time.

---

✅ Problem Solved: Baseball Game (LeetCode #682)

🐍 Language: Python

📅 Day 34 of Daily DSA Practice
