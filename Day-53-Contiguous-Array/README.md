# Day 53 of My DSA Journey 🚀

## Problem 53: Contiguous Array

### Difficulty
Medium

### Pattern
Prefix Sum + HashMap

### Problem Link

https://leetcode.com/problems/contiguous-array/

---

## Problem Statement

Given a binary array `nums` containing only `0`s and `1`s, return the maximum length of a contiguous subarray with an equal number of `0`s and `1`s.

A **contiguous subarray** means the elements are continuous without skipping any element.

---

## Example

### Input

```text
nums = [0,1,0]
```

### Output

```text
2
```

### Explanation

Possible valid subarrays are:

```text
[0,1]
```

and

```text
[1,0]
```

Both contain:

- One `0`
- One `1`

So the maximum length is:

```text
2
```

---

## Optimized Approach (Prefix Sum + HashMap)

The key observation is:

Instead of treating:

```text
0 as 0
1 as 1
```

we convert them into:

```text
0 → -1

1 → +1
```

Now if the running sum becomes the same at two different indices, it means the number of `0`s and `1`s between those indices is equal.

To solve the problem:

- Traverse the array once.
- Maintain a running prefix sum.
- Store the **first occurrence** of every prefix sum in a HashMap.
- Whenever the same prefix sum appears again, calculate the length of that subarray.
- Update the maximum length.

---

## Dry Run

### Input

```text
nums = [0,1,0]
```

### Initial Values

```text
prefix_sum = 0

max_length = 0

HashMap

{
0 : -1
}
```

---

### Step 1

Current element:

```text
0
```

Treat `0` as `-1`.

```text
prefix_sum = -1
```

HashMap does not contain `-1`.

Store:

```text
-1 : 0
```

---

### Step 2

Current element:

```text
1
```

Treat `1` as `+1`.

```text
prefix_sum = 0
```

HashMap already contains:

```text
0 : -1
```

Length:

```text
1 - (-1)

= 2
```

Update:

```text
max_length = 2
```

---

### Step 3

Current element:

```text
0
```

Treat `0` as `-1`.

```text
prefix_sum = -1
```

HashMap already contains:

```text
-1 : 0
```

Length:

```text
2 - 0

= 2
```

Maximum length remains:

```text
2
```

---

## Why Do We Convert `0` into `-1`?

Because we want equal numbers of `0`s and `1`s to produce a running sum of zero.

Example:

```text
0 1
```

becomes

```text
-1 + 1 = 0
```

Similarly,

```text
0 1 0 1
```

becomes

```text
-1 +1 -1 +1 = 0
```

Whenever the same prefix sum appears again, it means the subarray between those positions has equal numbers of `0`s and `1`s.

---

## Why Do We Store Only the First Index?

For each prefix sum, we store only its first occurrence.

The earliest occurrence gives the longest possible subarray when the same prefix sum appears again.

If we replace it with a later index, we may miss a longer valid subarray.

---

## Algorithm

For every element:

```text
1. If element is 0
      prefix_sum -= 1

2. Else
      prefix_sum += 1

3. Check whether prefix_sum already exists in the HashMap.

4. If it exists
      Calculate the length.

5. Update the maximum length.

6. Otherwise
      Store the current index as the first occurrence of the prefix sum.
```

---

## Time Complexity

```text
O(n)
```

The array is traversed only once.

---

## Space Complexity

```text
O(n)
```

The HashMap stores prefix sums and their first occurrence.

---

## What I Learned

- How Prefix Sum can solve problems beyond calculating sums.
- Why converting `0` to `-1` helps balance the number of `0`s and `1`s.
- How repeated prefix sums indicate a valid subarray.
- Why storing only the first occurrence of a prefix sum gives the longest answer.
- How HashMap helps achieve an `O(n)` solution.

---

✅ Problem Solved: Contiguous Array (LeetCode #525)

🐍 Language: Python

🧩 Pattern: Prefix Sum + HashMap

📅 Day 53 of Daily DSA Practice
