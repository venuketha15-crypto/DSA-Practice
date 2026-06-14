# Day 16 of My DSA Journey 🚀

## Problem 16: Group Anagrams

### Difficulty
Medium

### Problem Link

[LeetCode - Group Anagrams](https://leetcode.com/problems/group-anagrams/)

### Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **anagram** is a word formed by rearranging the letters of another word using exactly the same characters.

---

## Optimized Approach (Hash Map + Frequency Count)

- Create an empty dictionary to store groups of anagrams.
- Traverse each word in the input array.
- Create a frequency array of size 26 for each word.
- Count the occurrence of each character.
- Convert the frequency array into a tuple.
- Use the tuple as a dictionary key.
- If the key does not exist, create a new group.
- Add the current word to its corresponding group.
- Return all the grouped values.

---

## Example

### Input

```text
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

---

### Step 1: Process "eat"

Frequency Count:

```text
a = 1
e = 1
t = 1
```

Key:

```text
(1, 0, 0, 0, 1, ..., 1, ..., 0)
```

Dictionary:

```python
{
    key1: ["eat"]
}
```

---

### Step 2: Process "tea"

Frequency Count:

```text
a = 1
e = 1
t = 1
```

Same Key:

```text
(1, 0, 0, 0, 1, ..., 1, ..., 0)
```

Dictionary:

```python
{
    key1: ["eat", "tea"]
}
```

---

### Step 3: Process "tan"

Frequency Count:

```text
a = 1
n = 1
t = 1
```

Different Key:

```python
{
    key1: ["eat", "tea"],
    key2: ["tan"]
}
```

---

### Step 4: Process "ate"

Same frequency as `"eat"` and `"tea"`.

Dictionary:

```python
{
    key1: ["eat", "tea", "ate"],
    key2: ["tan"]
}
```

---

### Step 5: Process "nat"

Same frequency as `"tan"`.

Dictionary:

```python
{
    key1: ["eat", "tea", "ate"],
    key2: ["tan", "nat"]
}
```

---

### Step 6: Process "bat"

Different frequency.

Dictionary:

```python
{
    key1: ["eat", "tea", "ate"],
    key2: ["tan", "nat"],
    key3: ["bat"]
}
```

---

## Final Result

Output:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## Explanation

The key idea is that anagrams have exactly the same character frequencies.

For each word:

- Count how many times each letter appears.
- Convert the frequency list into a tuple.
- Use the tuple as a dictionary key.
- Words with the same key belong to the same group.

For example:

```text
eat → a=1, e=1, t=1
tea → a=1, e=1, t=1
ate → a=1, e=1, t=1
```

Since they have the same frequencies, they are grouped together.

## Time Complexity

```text
O(n × k)
```

Where:

- `n` = number of strings
- `k` = average length of each string

Reason:

- We traverse each word once.
- For each word, we traverse all its characters once.

---

## Space Complexity

```text
O(n × k)
```

Reason:

- The dictionary stores all grouped strings.

---

## What I Learned

- How to use hash maps to group similar data.
- Why tuples can be used as dictionary keys.
- Why lists cannot be dictionary keys.
- How frequency counting helps identify anagrams.
- How to solve Group Anagrams in O(n × k) time.
- Why this is the most optimized solution for this problem.

---

✅ Problem Solved: Group Anagrams (LeetCode #49)

🐍 Language: Python

📅 Day 16 of Daily DSA Practice
