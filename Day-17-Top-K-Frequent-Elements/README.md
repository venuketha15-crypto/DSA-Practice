# Day 17 of My DSA Journey 🚀

## Problem 17: Top K Frequent Elements

### Difficulty
Medium

### Problem Link

[LeetCode - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

### Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in any order.

---

## Optimized Approach (Bucket Sort)

- Count the frequency of each number using a hash map.
- Create buckets where the index represents the frequency.
- Place each number into its corresponding frequency bucket.
- Traverse the buckets from highest frequency to lowest frequency.
- Collect elements until `k` elements are found.
- Return the result.

---

## Example

### Input

```text
nums = [1,1,1,2,2,3]
k = 2
```

---

### Step 1: Count Frequencies

```python
count = {
    1: 3,
    2: 2,
    3: 1
}
```

Explanation:

```text
1 appears 3 times
2 appears 2 times
3 appears 1 time
```

---

### Step 2: Create Buckets

Since:

```text
len(nums) = 6
```

Create:

```python
freq = [[] for _ in range(len(nums) + 1)]
```

Buckets:

```python
[
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
```

---

### Step 3: Place Numbers into Buckets

```text
1 has frequency 3
```

```python
freq[3].append(1)
```

Buckets:

```python
[
    [],
    [],
    [],
    [1],
    [],
    [],
    []
]
```

---

```text
2 has frequency 2
```

```python
freq[2].append(2)
```

Buckets:

```python
[
    [],
    [],
    [2],
    [1],
    [],
    [],
    []
]
```

---

```text
3 has frequency 1
```

```python
freq[1].append(3)
```

Buckets:

```python
[
    [],
    [3],
    [2],
    [1],
    [],
    [],
    []
]
```

---

### Step 4: Traverse Buckets from Highest Frequency

Start from the end of the bucket array.

```text
Frequency 6 → Empty
Frequency 5 → Empty
Frequency 4 → Empty
Frequency 3 → Take 1
Result = [1]

Frequency 2 → Take 2
Result = [1, 2]
```

Since:

```text
len(result) == k
```

Stop and return the result.

---

## Final Output

```python
[1, 2]
```

---

## Explanation

The key idea is to group numbers based on their frequencies.

The bucket index represents the frequency, and the bucket stores all numbers having that frequency.

For example:

```text
Bucket 1 → Numbers appearing once
Bucket 2 → Numbers appearing twice
Bucket 3 → Numbers appearing three times
```

After filling the buckets, we traverse from the highest frequency bucket to get the top `k` frequent elements efficiently.

## Time Complexity

```text
O(n)
```

Where:

- `n` = length of the input array.

Reason:

- Counting frequencies → O(n)
- Filling buckets → O(n)
- Traversing buckets → O(n)

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

- Frequency dictionary stores the elements.
- Buckets store the elements based on frequency.
- Result array stores up to `k` elements.

---

## What I Learned

- How to use hash maps for frequency counting.
- What Bucket Sort is and how it works.
- Why the bucket index represents frequency.
- How to retrieve the top `k` frequent elements efficiently.
- Why this approach achieves O(n) time complexity.
- Why Bucket Sort is the optimal solution for this problem.

---

✅ Problem Solved: Top K Frequent Elements (LeetCode #347)

🐍 Language: Python

📅 Day 17 of Daily DSA Practice
