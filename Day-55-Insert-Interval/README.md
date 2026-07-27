# Day 55 of My DSA Journey 🚀

## Problem 55: Insert Interval

### Difficulty
Medium

### Pattern
Intervals

### Problem Link

[LeetCode - Insert Interval](https://leetcode.com/problems/insert-interval/)

---

## Problem Statement

You are given a list of **non-overlapping intervals** sorted in ascending order by their start time.

Insert a new interval into the list and merge any overlapping intervals so that the final list remains sorted and contains no overlapping intervals.

Return the updated list of intervals.

---

## Optimized Approach (One Pass)

Instead of inserting the new interval first and sorting the entire array again, we can solve the problem in **one traversal**.

The idea is:

- Add all intervals that come completely before the new interval.
- Merge every interval that overlaps with the new interval.
- Add the merged new interval.
- Add all remaining intervals.

Since every interval is processed only once, the solution runs in **O(n)** time.

---

## Example

### Input

```text
intervals = [[1,3],[6,9]]

newInterval = [2,5]
```

### Output

```text
[[1,5],[6,9]]
```

---

## Initial Values

Before traversing the intervals:

```text
merged = []

i = 0

n = 2

newInterval = [2,5]
```

---

## Step 1: Check Intervals Before newInterval

Current interval:

```text
[1,3]
```

Check:

```text
Current End < New Start

3 < 2
```

False.

This means the current interval is **not completely before** the new interval.

So we don't add it yet.

---

## Step 2: Merge Overlapping Intervals

Current interval:

```text
[1,3]
```

Check:

```text
Current Start <= New End

1 <= 5
```

True.

The intervals overlap.

Merge them.

Start becomes:

```text
min(2,1) = 1
```

End becomes:

```text
max(5,3) = 5
```

Now

```text
newInterval = [1,5]
```

Move to the next interval.

---

Current interval:

```text
[6,9]
```

Check:

```text
6 <= 5
```

False.

No more overlapping intervals.

---

## Step 3: Add the Merged Interval

```text
merged = [[1,5]]
```

---

## Step 4: Add Remaining Intervals

Current interval:

```text
[6,9]
```

Add it.

Now

```text
merged = [[1,5],[6,9]]
```

---

## Final Answer

```text
[[1,5],[6,9]]
```

---

## How the Algorithm Moves

```text
Start

        ↓

Add intervals that end before newInterval starts

        ↓

Merge all overlapping intervals

        ↓

Add the merged newInterval

        ↓

Add all remaining intervals

        ↓

Return Answer
```
---

## Time Complexity

```text
O(n)
```

### Reason

Each interval is visited only once.

---

## Space Complexity

```text
O(n)
```

### Reason

The output list stores the final merged intervals.

---

## What I Learned

- How to solve Insert Interval in one traversal.
- How to identify intervals before, overlapping with, and after the new interval.
- Why we compare the current interval's end with the new interval's start.
- Why we compare the current interval's start with the new interval's end.
- How merging updates the start using `min()` and the end using `max()`.
- How to solve interval problems efficiently without sorting again.

---

✅ Problem Solved: Insert Interval (LeetCode #57)

🐍 Language: Python

🧩 Pattern: Intervals

📅 Day 55 of Daily DSA Practice
