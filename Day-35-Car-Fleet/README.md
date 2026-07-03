# Day 35 of My DSA Journey 🚀

## Problem 35: Car Fleet

### Difficulty
Medium

### Problem Link

[LeetCode - Car Fleet](https://leetcode.com/problems/car-fleet/)

### Problem Statement

There are `n` cars traveling towards the same destination.

You are given:

- `target` – The destination.
- `position[]` – The starting position of each car.
- `speed[]` – The speed of each car.

A car **cannot overtake** another car. If a faster car catches a slower car before reaching the destination, they move together as one **car fleet**.

Return the total number of **car fleets** that will arrive at the destination.

---

## Optimized Approach (Sorting + Stack)

- Pair each car's position with its speed.
- Sort the cars by position in descending order (closest to the target first).
- Calculate the time each car needs to reach the destination.
- Use a stack to store the arrival time of each fleet.
- If the current car takes more time than the fleet ahead, it forms a new fleet.
- Otherwise, it joins the existing fleet.
- The size of the stack gives the total number of fleets.

---

## Example

### Input

```text
target = 12

position = [10,8,0,5,3]

speed = [2,4,1,1,3]
```

---

### Step 1

Pair position and speed.

```text
[(10,2), (8,4), (0,1), (5,1), (3,3)]
```

---

### Step 2

Sort by position (descending).

```text
[(10,2), (8,4), (5,1), (3,3), (0,1)]
```

---

### Step 3

Calculate arrival times.

```text
Position 10 → Time = 1

Position 8  → Time = 1

Position 5  → Time = 7

Position 3  → Time = 3

Position 0  → Time = 12
```

---

### Step 4

Process each car.

```text
Fleet Time Stack

[1]

[1]

[1,7]

[1,7]

[1,7,12]
```

---

### Final Answer

```text
3
```

There are **3 car fleets**.

---

## Explanation

The stack stores the **arrival time of each fleet**, not the individual cars.

- If the current car's arrival time is **greater** than the fleet ahead, it cannot catch up, so it forms a new fleet.
- If the current car's arrival time is **less than or equal to** the fleet ahead, it catches that fleet before reaching the destination and joins it.

At the end, the number of elements in the stack equals the number of fleets.

---

## Time Complexity

```text
O(n log n)
```

### Reason

- Sorting all cars takes **O(n log n)**.
- Traversing the sorted list takes **O(n)**.

Overall time complexity is:

```text
O(n log n)
```

---

## Space Complexity

```text
O(n)
```

### Reason

- The `cars` list stores all position-speed pairs.
- The stack stores the arrival time of each fleet.

---

## What I Learned

- How to solve problems using **Sorting + Stack**.
- How to pair two arrays using `zip()`.
- Why cars are processed from the closest to the target.
- Why the stack stores **fleet arrival times** instead of cars.
- How faster cars merge with slower cars to form fleets.
- Why the optimized solution has a time complexity of **O(n log n)**.

---

✅ Problem Solved: Car Fleet (LeetCode #853)

🐍 Language: Python

📅 Day 35 of Daily DSA Practice
```
