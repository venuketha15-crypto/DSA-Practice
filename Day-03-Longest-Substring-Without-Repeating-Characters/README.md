# Day 3 of My DSA Journey 🚀

## Problem 3: Longest Substring Without Repeating Characters

### Difficulty
Medium

### Problem Link

https://leetcode.com/problems/longest-substring-without-repeating-characters/

### Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

### Brute Force Approach

- I used two nested loops to generate all possible substrings.
- A set was used to keep track of characters in the current substring.
- If a duplicate character was found, I stopped expanding that substring.
- I continuously updated the maximum length of a valid substring.
- Although this approach works, it is not efficient for larger strings.

### Time Complexity of Brute Force

O(n²)

where n is the length of the string.

### Optimized Approach (Sliding Window)

- Since the brute-force solution has a higher time complexity, I used the Sliding Window technique.
- I maintained two pointers, `left` and `right`, to represent the current window.
- A set was used to store unique characters in the current window.
- If a duplicate character was found, I removed characters from the left side until the duplicate was removed.
- I continuously updated the maximum length of the valid window.
- This approach processes the string efficiently in a single pass.

### Example

Input:

s = "abcabcbb"

Step 1:

Window = "a"

Length = 1

Step 2:

Window = "ab"

Length = 2

Step 3:

Window = "abc"

Length = 3

Step 4:

Duplicate character 'a' found

Move left pointer

Window becomes "bca"

Output:

3

Explanation:

The longest substring without repeating characters is "abc".

Length = 3

### Time Complexity

O(n)

where n is the length of the string.

### Space Complexity

O(n)

A set is used to store unique characters in the current window.

### What I Learned

- How to generate substrings using nested loops.
- How sets help detect duplicate characters efficiently.
- How the Sliding Window technique works.
- How to optimize a brute-force solution from O(n²) to O(n).

✅ Problem Solved: Longest Substring Without Repeating Characters (LeetCode #3)

🐍 Language: Python

📅 Day 3 of Daily DSA Practice
