# Day 54 of My DSA Journey 🚀

## Problem 54: Merge Intervals

### Difficulty

Medium

### Problem Link

[LeetCode - Merge Intervals](https://leetcode.com/problems/merge-intervals/)

### Problem Statement

Given an array of intervals where each interval is represented as:

```text
[start, end]
```

Merge all overlapping intervals and return an array of the non-overlapping intervals.

---

### Approach

- Sort all intervals based on their starting value.
- Create an empty list called `merged`.
- Traverse each interval one by one.
- If `merged` is empty, add the current interval.
- Otherwise, compare the end of the last merged interval with the start of the current interval.
- If they overlap, merge them by updating the ending value.
- Otherwise, append the current interval to the list.
- After processing all intervals, return the merged list.

---

### Example

Input:

```text
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

After Sorting:

```text
[[1,3],[2,6],[8,10],[15,18]]
```

Create an empty list:

```text
merged = []
```

---

### Step 1

Current Interval:

```text
[1,3]
```

Since `merged` is empty,

Add it.

```text
merged = [[1,3]]
```

---

### Step 2

Current Interval:

```text
[2,6]
```

Compare:

```text
Last Interval = [1,3]

3 >= 2
```

They overlap.

Merge them.

```text
merged = [[1,6]]
```

---

### Step 3

Current Interval:

```text
[8,10]
```

Compare:

```text
Last Interval = [1,6]

6 < 8
```

They do not overlap.

Append it.

```text
merged = [[1,6],[8,10]]
```

---

### Step 4

Current Interval:

```text
[15,18]
```

Compare:

```text
Last Interval = [8,10]

10 < 15
```

They do not overlap.

Append it.

```text
merged = [[1,6],[8,10],[15,18]]
```

---

### Output

```text
[[1,6],[8,10],[15,18]]
```

---

### Explanation

The algorithm first sorts all intervals.

Sorting ensures that overlapping intervals appear next to each other.

For every interval:

- If it overlaps with the last merged interval, both intervals are combined into one.
- Otherwise, the current interval is added as a new interval.

For the input:

```text
[[1,3],[2,6],[8,10],[15,18]]
```

The first two intervals overlap:

```text
[1,3]

[2,6]
```

They are merged into:

```text
[1,6]
```

The remaining intervals do not overlap, so they remain unchanged.

Final answer:

```text
[[1,6],[8,10],[15,18]]
```

---

### Time Complexity

```text
O(n log n)
```

where `n` is the number of intervals.

Sorting takes:

```text
O(n log n)
```

Traversing the intervals takes:

```text
O(n)
```

Overall complexity:

```text
O(n log n)
```

---

### Space Complexity

```text
O(n)
```

The `merged` list stores the final merged intervals.

In the worst case, no intervals overlap, so all intervals are stored.

---

### What I Learned

- Why sorting is the first step in interval problems.
- How to identify overlapping intervals.
- How to merge two intervals into one.
- Why comparing only the last merged interval is enough.
- How sorting and a single traversal produce an efficient solution.

---

✅ Problem Solved: Merge Intervals (LeetCode #56)

🐍 Language: Python

🧩 Pattern: Intervals + Sorting

📅 Day 54 of Daily DSA Practice
