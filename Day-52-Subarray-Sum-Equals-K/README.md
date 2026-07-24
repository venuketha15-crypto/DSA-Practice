# Day 52 of My DSA Journey 🚀

## Problem 52: Subarray Sum Equals K

### Difficulty
Medium

### Pattern
Prefix Sum + HashMap

### Problem Link

[LeetCode - Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

---

## Problem Statement

Given an integer array `nums` and an integer `k`, find the total number of continuous subarrays whose sum is exactly equal to `k`.

A **subarray** is a continuous part of an array, meaning we cannot skip elements.

---

## Optimized Approach (Prefix Sum + HashMap)

The optimized approach uses **Prefix Sum + HashMap**.

The main idea is:

- Keep a running sum while moving through the array.
- Store every prefix sum and how many times it has appeared in a HashMap.
- At every position, calculate:

```text
needed = current_sum - k
```

- Check whether `needed` appeared earlier.
- If it appeared, valid subarray(s) with sum `k` exist.
- Add the frequency of `needed` to the answer.
- Store the current prefix sum for future use.

---

## Example

### Input

```text
nums = [1, 1, 1]
k = 2
```

Valid subarrays:

```text
[1, 1]      → Index 0 to 1 → Sum = 2

   [1, 1]   → Index 1 to 2 → Sum = 2
```

Therefore:

```text
Output = 2
```

---

## Initial Values

Before processing the array:

```text
prefix_count = {0: 1}

current_sum = 0

count = 0
```

Here:

- `current_sum` stores the running sum.
- `count` stores the number of valid subarrays found.
- `prefix_count` stores each prefix sum and how many times it has appeared.

We initially store:

```text
0 → 1
```

This helps us count valid subarrays that start from index `0`.

---

## Step 1: Process First Element

Current number:

```text
1
```

Update the running sum:

```text
current_sum = 0 + 1

current_sum = 1
```

Calculate:

```text
needed = current_sum - k

needed = 1 - 2

needed = -1
```

Check whether `-1` appeared before.

```text
No ❌
```

So:

```text
count = 0
```

Now remember that prefix sum `1` has appeared once.

```text
prefix_count:

0 → 1 time
1 → 1 time
```

---

## Step 2: Process Second Element

Current number:

```text
1
```

Update:

```text
current_sum = 1 + 1

current_sum = 2
```

Calculate:

```text
needed = 2 - 2

needed = 0
```

Check whether prefix sum `0` appeared before.

```text
Yes ✅

0 appeared 1 time
```

So we found one valid subarray:

```text
[1, 1]
 ↑  ↑
Index 0 to 1

Sum = 2
```

Increase:

```text
count = 1
```

Now remember prefix sum `2`.

```text
prefix_count:

0 → 1 time
1 → 1 time
2 → 1 time
```

---

## Step 3: Process Third Element

Current number:

```text
1
```

Update:

```text
current_sum = 2 + 1

current_sum = 3
```

Calculate:

```text
needed = 3 - 2

needed = 1
```

Check whether prefix sum `1` appeared before.

```text
Yes ✅

1 appeared 1 time
```

So another valid subarray exists:

```text
[1, 1]
 ↑  ↑
Index 1 to 2

Sum = 2
```

Increase:

```text
count = 2
```

Now remember prefix sum `3`.

---

## Final Output

```text
2
```

There are two subarrays whose sum equals `k`.

---

## Why Do We Calculate `current_sum - k`?

Suppose:

```text
current_sum = 3
k = 2
```

We need to know what previous prefix sum should be removed so that `2` remains.

```text
3 - ? = 2
```

The answer is:

```text
1
```

Therefore:

```text
needed = 3 - 2

needed = 1
```

If prefix sum `1` appeared earlier, then the elements after that prefix up to the current position have sum `2`.

The main relationship is:

```text
Current Prefix Sum - Previous Prefix Sum = k
```

Therefore:

```text
Previous Prefix Sum = Current Prefix Sum - k
```

---

## Why Do We Store Frequencies?

The same prefix sum can appear more than once.

For example:

```text
Prefix Sum 1 → appeared 2 times
```

If:

```text
needed = 1
```

then there are **2 possible previous positions** that can create valid subarrays ending at the current position.

Therefore, we add the number of times `needed` appeared.

```text
needed appeared 1 time → Add 1

needed appeared 2 times → Add 2

needed appeared 3 times → Add 3
```

This is why the HashMap stores:

```text
Prefix Sum → Frequency
```

and not just whether the prefix sum exists.

---

## How the Algorithm Works

At every element, we perform the same steps:

```text
1. Take the current number

2. Add it to current_sum

3. Calculate:

   needed = current_sum - k

4. Check whether needed exists
   in the HashMap

5. If it exists:
   Add its frequency to count

6. Store or update current_sum
   in the HashMap

7. Move to the next element
```

---

## Time Complexity

```text
O(n)
```

### Reason

We traverse the array only once.

For every element, HashMap lookup and update take approximately constant time.

Therefore:

```text
Overall = O(n)
```

---

## Space Complexity

```text
O(n)
```

### Reason

In the worst case, the HashMap may store different prefix sums for all elements.

---

## What I Learned

- How Prefix Sum works with a HashMap.
- How to maintain a running sum while traversing an array.
- How to count continuous subarrays with a target sum.
- Why we calculate `current_sum - k`.
- How a previous prefix sum helps identify a valid subarray.
- Why the HashMap starts with `0 → 1`.
- Why we store the frequency of each prefix sum.
- Why we add the frequency of `needed` instead of always adding only `1`.
- How the current prefix sum is stored for future elements.
- How Prefix Sum + HashMap reduces the solution to `O(n)` time.

---

✅ Problem Solved: Subarray Sum Equals K (LeetCode #560)

🐍 Language: Python

🧩 Pattern: Prefix Sum + HashMap

📅 Day 52 of Daily DSA Practice
