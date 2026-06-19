# Day 21 of My DSA Journey 🚀

## Problem 21: Longest Repeating Character Replacement

### Difficulty
Medium

### Problem Link

[LeetCode - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

### Problem Statement

You are given a string `s` and an integer `k`.

You can replace at most `k` characters in the string with any uppercase English character.

Return the length of the longest substring containing the same letter after performing at most `k` replacements.

---

## Optimized Approach (Sliding Window)

- Use a sliding window to maintain a valid substring.
- Keep track of the frequency of each character inside the current window.
- Find the frequency of the most common character in the window.
- Calculate how many replacements are needed to make all characters in the window the same.
- If the replacements needed exceed `k`, shrink the window from the left.
- Continuously update the maximum valid window length.

---

## Example

### Input

```text
s = "AABABBA"
k = 1
```

---

### Step 1: Start Expanding the Window

Window:

```text
A
```

Frequency:

```text
A = 1
```

Replacements Needed:

```text
0
```

Valid Window ✅

---

### Step 2: Continue Expanding

Window:

```text
AA
```

Frequency:

```text
A = 2
```

Replacements Needed:

```text
0
```

Valid Window ✅

---

### Step 3: Add Another Character

Window:

```text
AAB
```

Frequency:

```text
A = 2
B = 1
```

Most Frequent Character:

```text
A = 2
```

Replacements Needed:

```text
3 - 2 = 1
```

Valid Window ✅

---

### Step 4: Expand Further

Window:

```text
AABA
```

Frequency:

```text
A = 3
B = 1
```

Replacements Needed:

```text
4 - 3 = 1
```

Valid Window ✅

---

### Step 5: Window Becomes Invalid

Window:

```text
AABAB
```

Frequency:

```text
A = 3
B = 2
```

Replacements Needed:

```text
5 - 3 = 2
```

Since:

```text
2 > 1
```

The window becomes invalid.

Shrink the window from the left until it becomes valid again.

---

## Final Output

```text
4
```

---

## Explanation

The key idea is to make all characters in the current window equal.

To determine how many replacements are needed:

```text
Window Size - Frequency of Most Common Character
```

If the replacements required are less than or equal to `k`, the window is valid.

Otherwise, the window must be shrunk.

This allows us to efficiently find the longest valid substring.

---

## Time Complexity

```text
O(n)
```

Where:

- `n` = length of the string.

Reason:

- Each character enters the window once.
- Each character leaves the window at most once.

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

- Only character frequencies are stored.
- At most 26 uppercase English letters exist.

---

## What I Learned

- How Sliding Window works.
- How to track character frequencies using a Hash Map.
- How to maintain a valid window.
- When to expand and shrink the window.
- How to calculate the number of replacements needed.
- Why this approach achieves O(n) time complexity.

---

✅ Problem Solved: Longest Repeating Character Replacement (LeetCode #424)

🐍 Language: Python

📅 Day 21 of Daily DSA Practice
