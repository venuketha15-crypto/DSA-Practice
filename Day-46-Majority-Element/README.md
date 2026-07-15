# Day 46 of My DSA Journey 🚀

## Problem 46: Majority Element

### Difficulty
Easy

### Problem Link

[LeetCode - Majority Element](https://leetcode.com/problems/majority-element/)

---

## Problem Statement

Given an integer array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than** `⌊n / 2⌋` times.

You can assume that the majority element always exists in the array.

---

# Approach 1: Hash Map (Frequency Counting)

## Idea

- Create a dictionary to count the frequency of every element.
- Traverse the array.
- Increase the frequency of the current element.
- If the frequency becomes greater than `len(nums) // 2`, return that element.

### Example

```text
nums = [2,2,1,1,1,2,2]

Read 2
{2:1}

Read 2
{2:2}

Read 1
{2:2,1:1}

Read 1
{2:2,1:2}

Read 1
{2:2,1:3}

Read 2
{2:3,1:3}

Read 2
{2:4,1:3}

7 // 2 = 3

4 > 3 ✅

Answer = 2
```

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

---

# Approach 2: Boyer-Moore Voting Algorithm (Optimized)

## Idea

- Maintain two variables:
  - `candidate`
  - `count`
- If `count` becomes `0`, choose the current element as the new candidate.
- If the current element equals the candidate, increase `count`.
- Otherwise, decrease `count`.
- The remaining candidate is the majority element.

### Example

```text
nums = [2,2,1,1,1,2,2]
```

```text
Read 2

candidate = 2
count = 1
```

```text
Read 2

Same candidate

count = 2
```

```text
Read 1

Different

count = 1
```

```text
Read 1

Different

count = 0
```

Choose next element as candidate.

```text
Read 1

candidate = 1
count = 1
```

```text
Read 2

Different

count = 0
```

Choose next element as candidate.

```text
Read 2

candidate = 2
count = 1
```

Final Answer

```text
2
```

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(1)
```

---

## What I Learned

- How to solve the problem using a Hash Map.
- How frequency counting works.
- Why the Hash Map solution uses extra space.
- How the Boyer-Moore Voting Algorithm eliminates extra space.
- Why the majority element cannot be completely canceled out.
- Difference between **O(n)** space and **O(1)** space solutions.

---

✅ Problem Solved: Majority Element (LeetCode #169)

🐍 Language: Python

📅 Day 46 of Daily DSA Practice
