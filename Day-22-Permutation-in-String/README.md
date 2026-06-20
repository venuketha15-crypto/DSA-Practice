# Day 22 of My DSA Journey 🚀

## Problem 22: Permutation in String

### Difficulty
Medium

### Problem Link

[LeetCode - Permutation in String](https://leetcode.com/problems/permutation-in-string/)

### Problem Statement

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

A permutation is a rearrangement of all the characters of a string.

---

## Optimized Approach (Sliding Window + Frequency Array)

- Create a frequency array for `s1`.
- Create another frequency array for the current window in `s2`.
- Use a fixed-size sliding window of length `len(s1)`.
- Compare the frequencies of the current window and `s1`.
- If both frequencies match, a permutation is found.
- Otherwise, slide the window by adding a new character and removing the old character.
- Continue until all windows are checked.

---

## Example

### Input

```text
s1 = "ab"
s2 = "eidbaooo"
```

---

### Step 1: Create Frequency of s1

```text
a = 1
b = 1
```

---

### Step 2: Check First Window

Window:

```text
ei
```

Frequency:

```text
e = 1
i = 1
```

Compare with:

```text
a = 1
b = 1
```

Not Equal ❌

---

### Step 3: Slide Window

Window:

```text
id
```

Frequency:

```text
i = 1
d = 1
```

Not Equal ❌

---

### Step 4: Slide Window Again

Window:

```text
db
```

Frequency:

```text
d = 1
b = 1
```

Not Equal ❌

---

### Step 5: Slide Window Again

Window:

```text
ba
```

Frequency:

```text
b = 1
a = 1
```

Compare with:

```text
a = 1
b = 1
```

Equal ✅

Permutation Found.

Return:

```text
True
```

---

## Final Output

```text
True
```

---

## Explanation

The key idea is that two strings are permutations of each other if they contain the same characters with the same frequencies.

Instead of generating all possible permutations, we compare frequency counts using a fixed-size sliding window.

Whenever the frequency of the current window matches the frequency of `s1`, a permutation exists in `s2`.

---

## Time Complexity

```text
O(n)
```

Where:

- `n` = length of `s2`

Reason:

- Each character enters the window once.
- Each character leaves the window once.

Overall:

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

Reason:

- Frequency arrays have a fixed size of 26 for lowercase English letters.

---

## What I Learned

- What permutations are.
- How to compare strings using frequency counts.
- How fixed-size Sliding Window works.
- How to efficiently update frequencies while moving the window.
- Why frequency arrays are useful for character-based problems.
- How this approach achieves O(n) time complexity.

---

✅ Problem Solved: Permutation in String (LeetCode #567)

🐍 Language: Python

📅 Day 22 of Daily DSA Practice
