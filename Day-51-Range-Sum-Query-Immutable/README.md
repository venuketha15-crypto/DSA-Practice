# Day 51 of My DSA Journey 🚀

## Problem 51: Range Sum Query - Immutable

### Difficulty
Easy

### Pattern
Prefix Sum

### Problem Link

[LeetCode - Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

---

## Problem Statement

Given an integer array `nums`, we need to answer multiple queries.

For each query:

```text
sumRange(left, right)
```

we need to return the sum of all elements from index `left` to index `right`, including both positions.

Instead of calculating the sum again for every query, we can use the **Prefix Sum** technique to answer each query efficiently.

---

## Optimized Approach (Prefix Sum)

The main idea is:

- Create a prefix sum array once.
- Start the prefix array with an extra `0`.
- Store the cumulative sum of elements.
- For every range query, subtract the unwanted portion before `left`.
- This allows every `sumRange()` query to be answered in `O(1)` time.

The range sum is calculated using:

```text
prefix[right + 1] - prefix[left]
```

---

## Example

### Input

```text
nums = [-2, 0, 3, -5, 2, -1]
```

Suppose we want:

```text
sumRange(2, 5)
```

We need the sum of elements from index `2` to index `5`.

```text
Index:    0    1    2    3    4    5

nums =  [-2,   0,   3,  -5,   2,  -1]
                    └────────────────┘
                          WANT
```

So:

```text
3 + (-5) + 2 + (-1)

= -1
```

---

## Step 1: Create the Prefix Array

Start with an extra `0`:

```python
prefix = [0]
```

Initially:

```text
prefix = [0]
```

The extra `0` makes range calculations easier, especially when `left = 0`.

---

## Step 2: Build Prefix Sums

For every number, add:

```text
Previous Prefix Sum + Current Number
```

### First Number: `-2`

```text
0 + (-2) = -2
```

Prefix becomes:

```text
[0, -2]
```

---

### Second Number: `0`

```text
-2 + 0 = -2
```

Prefix becomes:

```text
[0, -2, -2]
```

---

### Third Number: `3`

```text
-2 + 3 = 1
```

Prefix becomes:

```text
[0, -2, -2, 1]
```

---

### Fourth Number: `-5`

```text
1 + (-5) = -4
```

Prefix becomes:

```text
[0, -2, -2, 1, -4]
```

---

### Fifth Number: `2`

```text
-4 + 2 = -2
```

Prefix becomes:

```text
[0, -2, -2, 1, -4, -2]
```

---

### Sixth Number: `-1`

```text
-2 + (-1) = -3
```

Final prefix array:

```text
[0, -2, -2, 1, -4, -2, -3]
```

---

## Step 3: Understand the Prefix Array

Original array:

```text
nums index:       0    1    2    3    4    5

nums:            -2    0    3   -5    2   -1
```

Prefix array:

```text
prefix index:  0    1    2    3    4    5    6

prefix:        0   -2   -2    1   -4   -2   -3
               ↑
            Extra 0
```

Because of the extra `0`, the prefix array is shifted by one position.

For example:

```text
prefix[1] = Sum through nums[0]

prefix[2] = Sum through nums[1]

prefix[3] = Sum through nums[2]

prefix[4] = Sum through nums[3]
```

So:

```text
nums[i] → included through prefix[i + 1]
```

---

## Step 4: Calculate `sumRange(2, 5)`

We want:

```text
Index 2 → Index 5
```

Use:

```text
prefix[right + 1] - prefix[left]
```

Here:

```text
left = 2
right = 5
```

Therefore:

```text
prefix[5 + 1] - prefix[2]

= prefix[6] - prefix[2]
```

From our prefix array:

```text
prefix[6] = -3

prefix[2] = -2
```

So:

```text
-3 - (-2)

= -1
```

Therefore:

```text
sumRange(2, 5) = -1
```

---

## Why Does Subtraction Work?

`prefix[6]` contains the sum of:

```text
[-2, 0, 3, -5, 2, -1]
 └────────────────────┘
       EVERYTHING
```

But we only want:

```text
[3, -5, 2, -1]
 └────────────┘
      WANT
```

The unwanted part is:

```text
[-2, 0]
 └────┘
 REMOVE
```

So we calculate:

```text
Everything
    -
Unwanted Beginning
    =
Wanted Range
```

That is:

```text
prefix[right + 1] - prefix[left]
```

---

## Why Do We Add an Extra `0`?

Suppose:

```text
sumRange(0, 2)
```

We want:

```text
-2 + 0 + 3 = 1
```

Using the same formula:

```text
prefix[right + 1] - prefix[left]

= prefix[3] - prefix[0]

= 1 - 0

= 1
```

So the extra `0` allows us to use the same formula even when:

```text
left = 0
```

We do not need a separate special condition.

---

## Time Complexity

### Building the Prefix Array

```text
O(n)
```

Reason:

We visit every element of `nums` once.

---

### Each `sumRange()` Query

```text
O(1)
```

Reason:

We only perform:

```text
One lookup
One lookup
One subtraction
```

We do not loop through the requested range.

This is the main advantage of Prefix Sum.

---

## Space Complexity

```text
O(n)
```

Reason:

We create a prefix array containing cumulative sums for the input elements.

---

## What I Learned

- What the Prefix Sum pattern is.
- How to build a prefix sum array.
- How a running sum stores previous calculations.
- Why adding an extra `0` makes range queries easier.
- Why the prefix array has one extra position compared to the original array.
- How to calculate a range sum using subtraction.
- Why `right + 1` is used when an extra `0` is added.
- How `self.prefix[-1]` gives the previously calculated prefix sum.
- How `self.prefix` allows the prefix array created in `__init__()` to be used later in `sumRange()`.
- How preprocessing in `O(n)` allows each future range query to be answered in `O(1)` time.

---

✅ Problem Solved: Range Sum Query - Immutable (LeetCode #303)

🐍 Language: Python

🧩 Pattern: Prefix Sum

📅 Day 51 of Daily DSA Practice
