# Day 15 of My DSA Journey 🚀

## Problem 15: Valid Anagram

### Difficulty
Easy

### Problem Link

[LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/)

### Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another word, using all the original letters exactly once.

### Brute Force Approach

- Check if both strings have the same length.
- Convert `t` into a list.
- Traverse each character in `s`.
- If the character exists in `t`, remove its first occurrence.
- If the character does not exist, return `False`.
- If all characters are matched successfully, return `True`.

### Time Complexity of Brute Force

```text
O(n²)
```

- Checking `ch in t` takes O(n).
- Removing an element from a list also takes O(n).

### Space Complexity of Brute Force

```text
O(n)
```

Extra space is used to store `t` as a list.

### Optimized Approach (Hash Map)

- Check if both strings have the same length.
- Create a dictionary to store character frequencies.
- Traverse the first string and increase the frequency of each character.
- Traverse the second string and decrease the frequency of each character.
- If a character does not exist in the dictionary, return `False`.
- If any frequency becomes negative, return `False`.
- If all checks pass, return `True`.

### Example

Input:

```text
s = "anagram"
t = "nagaram"
```

### Step 1: Check Length

```text
len(s) = 7
len(t) = 7
```

Since both lengths are equal, continue.

### Step 2: Build Frequency Dictionary

Start with:

```python
count = {}
```

Process `"anagram"`:

```text
'a' → {'a': 1}

'n' → {'a': 1, 'n': 1}

'a' → {'a': 2, 'n': 1}

'g' → {'a': 2, 'n': 1, 'g': 1}

'r' → {'a': 2, 'n': 1, 'g': 1, 'r': 1}

'a' → {'a': 3, 'n': 1, 'g': 1, 'r': 1}

'm' → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
```

Final Dictionary:

```python
{
    'a': 3,
    'n': 1,
    'g': 1,
    'r': 1,
    'm': 1
}
```

### Step 3: Process the Second String

Traverse `"nagaram"`:

```text
'n' → count becomes 0

'a' → count becomes 2

'g' → count becomes 0

'a' → count becomes 1

'r' → count becomes 0

'a' → count becomes 0

'm' → count becomes 0
```

Final Dictionary:

```python
{
    'a': 0,
    'n': 0,
    'g': 0,
    'r': 0,
    'm': 0
}
```

All frequencies match.

### Final Result

Output:

```text
True
```

### Explanation

The brute-force approach repeatedly searches and removes characters, resulting in O(n²) time complexity.

The optimized approach uses a hash map to count character frequencies.

We first count how many times each character appears in the first string. Then, while traversing the second string, we decrease those frequencies.

If a character is missing or its frequency becomes negative, the strings cannot be anagrams.

Otherwise, both strings contain exactly the same characters with the same frequencies.

### Time Complexity

```text
O(n)
```

where `n` is the length of the strings.

- One pass through `s`
- One pass through `t`

### Space Complexity

```text
O(1)
```

Since the strings contain only lowercase English letters, the dictionary stores at most 26 characters.

### What I Learned

- How to solve Valid Anagram using a brute-force approach.
- Why `remove()` leads to O(n²) complexity.
- How to use hash maps for frequency counting.
- What `dictionary.get(key, default)` means.
- Why checking string lengths first is important.
- How to optimize a solution from O(n²) to O(n).
- Why hash maps are powerful for string problems.

✅ Problem Solved: Valid Anagram (LeetCode #242)

🐍 Language: Python

📅 Day 15 of Daily DSA Practice
