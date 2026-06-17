# Day 19 of My DSA Journey 🚀

## Problem 19: Longest Consecutive Sequence

### Difficulty
Medium

### Problem Link

[LeetCode - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

### Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time complexity.

---

## Optimized Approach (Hash Set)

### Key Observation

Instead of sorting the array, use a Hash Set because it provides O(1) lookup.

A number is considered the **start of a sequence** only if:

```text
num - 1 does not exist in the set.
```

If the previous number exists, then the current number is already part of another sequence, so we skip it.

---

## Example

### Input

```text
nums = [100, 4, 200, 1, 3, 2]
```

Convert the array into a set:

```text
{100, 4, 200, 1, 3, 2}
```

---

## Finding the Start of Sequences

### Number = 100

Check:

```text
99 exists?
```

Answer:

```text
No
```

Therefore:

```text
100 is the start of a sequence.
```

Sequence:

```text
100
```

Length:

```text
1
```

Longest Length:

```text
1
```

---

### Number = 4

Check:

```text
3 exists?
```

Answer:

```text
Yes
```

Therefore:

```text
4 is not the start of a sequence.
```

Skip it.

---

### Number = 200

Check:

```text
199 exists?
```

Answer:

```text
No
```

Therefore:

```text
200 is the start of a sequence.
```

Sequence:

```text
200
```

Length:

```text
1
```

Longest Length:

```text
1
```

---

### Number = 1

Check:

```text
0 exists?
```

Answer:

```text
No
```

Therefore:

```text
1 is the start of a sequence.
```

Sequence:

```text
1 → 2 → 3 → 4
```

Length:

```text
4
```

Longest Length:

```text
4
```

---

## Final Answer

```text
4
```

Because the longest consecutive sequence is:

```text
1 → 2 → 3 → 4
```

---

## Why Do We Check `num - 1`?

Suppose we have:

```text
1 → 2 → 3 → 4
```

For:

```text
2
```

Since:

```text
1 exists
```

2 is not the start.

For:

```text
3
```

Since:

```text
2 exists
```

3 is not the start.

For:

```text
4
```

Since:

```text
3 exists
```

4 is not the start.

Only:

```text
1
```

has no previous number.

Therefore:

```text
1 is the true start of the sequence.
```

This helps us avoid counting the same sequence multiple times.

---

## Another Example

### Input

```text
nums = [4, 3, 2]
```

Set:

```text
{2, 3, 4}
```

Check:

```text
4 → 3 exists → Skip
3 → 2 exists → Skip
2 → 1 does not exist → Start sequence
```

Sequence:

```text
2 → 3 → 4
```

Length:

```text
3
```

Answer:

```text
3
```

---

## Time Complexity

```text
O(n)
```

Reason:

- Creating the Hash Set takes O(n).
- Each number is processed at most once.

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

Reason:

- The Hash Set stores all elements from the array.

---

## What I Learned

- How Hash Sets provide O(1) lookup.
- How to identify the true start of a sequence.
- Why checking `num - 1` avoids repeated work.
- Why sorting is not necessary.
- How to efficiently find the longest consecutive sequence.
- How to achieve O(n) time complexity.
- Why this is the optimal approach for LeetCode 128.

---

✅ Problem Solved: Longest Consecutive Sequence (LeetCode #128)

🐍 Language: Python

📅 Day 19 of Daily DSA Practice
