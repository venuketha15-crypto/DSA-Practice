# Day 45 of My DSA Journey 🚀

## Problem 45: Minimum Window Substring

### Difficulty
Hard

### Problem Link

[LeetCode - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

---

## Problem Statement

Given two strings `s` and `t`, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window.

If there is no such substring, return an empty string `""`.

---

## Optimized Approach (Sliding Window + Hash Map)

- Create a frequency map for the characters in `t`.
- Use another frequency map to track the current window.
- Expand the window by moving the `right` pointer.
- Whenever a required character reaches its required frequency, increase `have`.
- Once all required characters are present (`have == needCount`):
  - Update the minimum window if the current window is smaller.
  - Shrink the window from the left.
  - If removing a character makes the window invalid, decrease `have`.
- Continue until the end of the string.

---

## Example

### Input

```text
s = "ADOBECODEBANC"
t = "ABC"
```

---

### Step 1

```text
Window:

A D O B E C

Characters Found:
A ✅
B ✅
C ✅

Current Window = "ADOBEC"
Length = 6
```

This is the first valid window.

---

### Step 2

Shrink the window by moving the `left` pointer.

```text
Remove A

Window:

D O B E C
```

Now the window no longer contains `A`.

```text
A ❌
B ✅
C ✅
```

The window becomes invalid, so stop shrinking.

---

### Step 3

Continue expanding the window by moving the `right` pointer.

Eventually, the window becomes:

```text
B A N C
```

Characters Found:

```text
A ✅
B ✅
C ✅
```

Length:

```text
4
```

Since:

```text
4 < 6
```

Update the answer.

---

## Final Output

```text
BANC
```

The smallest substring containing all characters of `"ABC"` is:

```text
BANC
```

---

## Explanation

The Sliding Window technique maintains a valid window that contains all required characters.

- Expand the window using the `right` pointer.
- Count character frequencies in the current window.
- Once all required characters are included, shrink the window using the `left` pointer.
- Keep updating the smallest valid window found.

This avoids checking every possible substring and makes the solution efficient.

---

## Time Complexity

```text
O(n)
```

### Reason

Each character enters and leaves the sliding window at most once.

---

## Space Complexity

```text
O(m)
```

### Reason

Two hash maps are used to store character frequencies, where `m` is the number of unique characters.

---

## What I Learned

- How to use two frequency maps in a Sliding Window problem.
- The purpose of `have` and `needCount`.
- When to expand and shrink the window.
- How to find the smallest valid substring efficiently.
- How to solve an advanced Sliding Window problem in **O(n)** time.

---

✅ Problem Solved: Minimum Window Substring (LeetCode #76)

🐍 Language: Python

📅 Day 45 of Daily DSA Practice
