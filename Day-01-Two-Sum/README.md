# Day 1 of My DSA Journey 🚀

Hi, I'm Venu, a B.Tech CSE (AIML) student.
I have started my DSA journey to improve my problem-solving skills and prepare for technical interviews. In this repository, I will share my daily DSA solutions, approaches, examples, and learnings.

## Problem 1: Two Sum

### Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.
You may assume that each input has exactly one solution, and you may not use the same element twice.

### Approach

* I used a dictionary (hash map) to store numbers and their indices.
* For each number, I calculated the complement using `target - current_number`.
* If the complement was already present in the dictionary, I returned the indices.
* Otherwise, I stored the current number and its index.
* This approach solves the problem in a single pass through the array.

### Example

Input:
nums = [2, 7, 11, 15]
target = 9

Step 1:

* Current number = 2
* Complement = 7
* 7 is not found
* Store {2: 0}

Step 2:

* Current number = 7
* Complement = 2
* 2 is found in the dictionary

Output: [0, 1]

Explanation:
2 + 7 = 9, therefore the indices of the required numbers are 0 and 1.

### Time Complexity  :  O(n)
### Space Complexity :  O(n)

### What I Learned
* How to use a dictionary (hash map) for fast lookups.
* How to optimize a brute-force approach from O(n²) to O(n).
* How to track previously seen elements while iterating through an array.

✅ Problem Solved: Two Sum (LeetCode #1)
🐍 Language: Python
📅 Day 1 of Daily DSA Practice
