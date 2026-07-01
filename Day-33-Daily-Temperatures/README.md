# Day 33 of My DSA Journey 🚀

## Problem 33: Daily Temperatures

### Difficulty
Medium

### Problem Link

[LeetCode - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

### Problem Statement

Given an array of integers `temperatures`, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `iᵗʰ` day to get a warmer temperature.

If there is no future day with a warmer temperature, keep the answer as `0`.

---

## Optimized Approach (Monotonic Stack)

- Create an answer array initialized with `0`.
- Use a stack to store the **indices** of days waiting for a warmer temperature.
- Traverse the temperature array from left to right.
- If the current temperature is warmer than the temperature at the index on the top of the stack:
  - Pop the index.
  - Calculate the number of days waited.
  - Store it in the answer array.
- Repeat until the stack becomes empty or the current temperature is no longer warmer.
- Push the current index onto the stack.

---

## Example

### Input

```text
temperatures = [73,74,75,71,69,72,76,73]
```

---

### Step 1

Day 0

```text
Stack = [0]
Answer = [0,0,0,0,0,0,0,0]
```

---

### Step 2

Current temperature = 74

```text
74 > 73
```

Pop index `0`

```text
Answer[0] = 1
```

Push index `1`

```text
Stack = [1]
Answer = [1,0,0,0,0,0,0,0]
```

---

### Step 3

Current temperature = 75

```text
75 > 74
```

Pop index `1`

```text
Answer[1] = 1
```

Push index `2`

```text
Stack = [2]
Answer = [1,1,0,0,0,0,0,0]
```

---

### Step 4

Current temperature = 71

```text
71 < 75
```

Push index `3`

```text
Stack = [2,3]
```

---

### Step 5

Continue until the end.

Final Answer

```text
[1,1,4,2,1,1,0,0]
```

---

## Explanation

This problem is solved using a **Monotonic Stack**.

The stack stores **indices**, not temperatures.

For every new temperature:

- Compare it with the temperature at the index on the top of the stack.
- If it is warmer, pop the index and calculate the waiting days.
- Continue until the stack is empty or the current temperature is not warmer.
- Push the current day's index onto the stack.

Each index is pushed once and popped once, making the solution efficient.

---

## Time Complexity

```text
O(n)
```

### Reason

- Every index is pushed into the stack exactly once.
- Every index is popped from the stack at most once.
- Therefore, each element is processed at most two times.

---

## Space Complexity

```text
O(n)
```

### Reason

In the worst case (temperatures are in decreasing order), every index is stored in the stack.

Example:

```text
[80,79,78,77,76]
```

The stack contains all indices.

---

## What I Learned

- How a Monotonic Stack works.
- Why we store **indices instead of temperatures**.
- How to find the next warmer temperature efficiently.
- Why `while` is used instead of `if`.
- How each index is pushed and popped only once.
- Why the optimized solution runs in **O(n)** time.

---

✅ Problem Solved: Daily Temperatures (LeetCode #739)

🐍 Language: Python

📅 Day 33 of Daily DSA Practice
