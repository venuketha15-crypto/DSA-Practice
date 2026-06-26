# Day 28 of My DSA Journey 🚀

## Problem 28: Time Based Key-Value Store

### Difficulty
Medium

### Problem Link

[LeetCode - Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

### Problem Statement

Design a time-based key-value data structure that supports the following operations:

- `set(key, value, timestamp)` – Stores the key with its value and timestamp.
- `get(key, timestamp)` – Returns the value associated with the largest timestamp less than or equal to the given timestamp.

If no such timestamp exists, return an empty string.

---

## Optimized Approach (Hash Map + Binary Search)

- Use a Hash Map where each key stores a list of `(timestamp, value)` pairs.
- Since timestamps are added in increasing order, the list remains sorted.
- For the `set()` operation, simply append the new `(timestamp, value)` pair.
- For the `get()` operation, perform Binary Search on the timestamp list.
- Find the largest timestamp less than or equal to the given timestamp.
- Return the corresponding value.

---

## Example

### Operations

```text
set("foo", "bar", 1)
set("foo", "bar2", 4)
set("foo", "bar3", 7)
```

Stored Data

```text
foo

Timestamp  Value
1          bar
4          bar2
7          bar3
```

---

### Query

```text
get("foo", 6)
```

---

### Step 1

```text
left = 0
right = 2
```

Find middle:

```text
mid = 1
```

Check:

```text
Timestamp = 4
```

Since:

```text
4 <= 6
```

Store:

```text
result = "bar2"
```

Search for a larger valid timestamp.

Move:

```text
left = 2
```

---

### Step 2

```text
left = 2
right = 2
```

Find middle:

```text
mid = 2
```

Check:

```text
Timestamp = 7
```

Since:

```text
7 > 6
```

Move:

```text
right = 1
```

The loop ends.

---

## Final Output

```text
bar2
```

---

## Explanation

The key idea is to store all values for a key along with their timestamps.

Since timestamps are stored in increasing order, Binary Search can efficiently find the latest timestamp that is less than or equal to the requested timestamp.

This avoids checking every timestamp one by one and makes the `get()` operation much faster.

---

## Time Complexity

### set()

```text
O(1)
```

### get()

```text
O(log n)
```

Where `n` is the number of timestamps stored for a key.

---

## Space Complexity

```text
O(n)
```

Where `n` is the total number of `(timestamp, value)` pairs stored.

---

## What I Learned

- How to design a time-based key-value data structure.
- How to use a Hash Map to organize data.
- How Binary Search finds the latest valid timestamp efficiently.
- Why timestamps must be stored in sorted order.
- Difference between exact timestamp search and finding the largest timestamp less than or equal to a given value.
- How combining Hash Maps and Binary Search improves performance.

---

✅ Problem Solved: Time Based Key-Value Store (LeetCode #981)

🐍 Language: Python

📅 Day 28 of Daily DSA Practice
