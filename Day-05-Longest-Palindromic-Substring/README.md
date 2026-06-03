# Day 5 of My DSA Journey 🚀

## Problem 5: Longest Palindromic Substring

### Difficulty
Medium

### Problem Link

https://leetcode.com/problems/longest-palindromic-substring/

### Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same forward and backward.

### Brute Force Approach

- Generate all possible substrings.
- Check whether each substring is a palindrome.
- Keep track of the longest palindrome found.
- Although this approach works, it becomes inefficient for larger strings.

### Time Complexity of Brute Force

O(n³)

where n is the length of the string.

### Optimized Approach (Expand Around Center)

- Every palindrome has a center.
- I considered each character as the center of a palindrome.
- First, I checked for odd-length palindromes by expanding from the same index.
- Then, I checked for even-length palindromes by expanding from two adjacent indices.
- Whenever a longer palindrome was found, I updated the result.
- Finally, I returned the longest palindromic substring.

### Example

Input:

s = "babad"

Initial:

```text
res = ""
```

Step 1:

```python
i = 0
```

Odd Length Palindrome:

```python
l = r = 0
```

Palindrome found:

```text
"b"
```

Update:

```python
res = "b"
```

---

Step 2:

```python
i = 1
```

Odd Length Palindrome:

```python
l = r = 1
```

Current character:

```text
"a"
```

Expand outward:

```python
l = 0
r = 2
```

Characters:

```text
s[l] = 'b'
s[r] = 'b'
```

They match ✅

Palindrome found:

```text
"bab"
```

Update:

```python
res = "bab"
```

Expand again:

```python
l = -1
r = 3
```

Stop because the left pointer is out of bounds.

---

Step 3:

```python
i = 2
```

Odd Length Palindrome:

```python
l = r = 2
```

Current character:

```text
"b"
```

Expand outward:

```python
l = 1
r = 3
```

Characters:

```text
s[l] = 'a'
s[r] = 'a'
```

They match ✅

Palindrome found:

```text
"aba"
```

Length = 3

Current result:

```text
"bab"
```

Since both palindromes have the same length, the result remains unchanged.

---

Step 4:

The algorithm continues checking all remaining centers and no longer palindrome is found.

Output:

```text
"bab"
```

### Explanation

The algorithm treats every character as a possible center of a palindrome.

For center `"a"` (index 1), it expands outward and finds:

```text
"bab"
```

For center `"b"` (index 2), it expands outward and finds:

```text
"aba"
```

Both are valid palindromes of length 3.

Since no longer palindrome exists in the string, the algorithm returns one of them.

Therefore, the answer is:

```text
"bab"
```

(Another valid answer is `"aba"`.)

### Note

Even-length expansion is also checked at every index using:

```python
l = i
r = i + 1
```

However, for the input `"babad"`, no even-length palindrome longer than the current result is found.

### Time Complexity

O(n²)

where n is the length of the string.

For each character, we may expand outward across the string.

### Space Complexity

O(1)

No extra data structure is used apart from a few variables.

### What I Learned

- How palindromes work.
- How to expand around a center.
- The difference between odd-length and even-length palindromes.
- How to optimize a brute-force solution from O(n³) to O(n²).
- How to find the longest palindromic substring efficiently.

✅ Problem Solved: Longest Palindromic Substring (LeetCode #5)

🐍 Language: Python

📅 Day 5 of Daily DSA Practice
