# Day 2 of My DSA Journey 🚀

## Problem 2: Add Two Numbers

### Difficulty
Medium

### Problem Link

[LeetCode - Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

### Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

### Approach

- I created a dummy node to build the result linked list.
- I used a carry variable to store the carry generated during addition.
- I traversed both linked lists simultaneously.
- At each step, I added the values from both linked lists along with the carry.
- I stored the resulting digit in a new node.
- The carry was passed to the next iteration.
- Finally, I returned the result linked list starting from `dummy.next`.

### Example

Input:

l1 = [2,4,3]

l2 = [5,6,4]

Step 1:

2 + 5 = 7

Result = [7]

Step 2:

4 + 6 = 10

Digit = 0

Carry = 1

Result = [7,0]

Step 3:

3 + 4 + 1 = 8

Result = [7,0,8]

Output:

[7,0,8]

Explanation:

The linked lists represent the numbers 342 and 465.

342 + 465 = 807

### Time Complexity

O(max(n,m))

where n and m are the lengths of the two linked lists.

### Space Complexity

O(max(n,m))

A new linked list is created to store the result, so the space depends on the size of the output list.

### What I Learned

- How to work with linked lists.
- How to handle carry during addition.
- How dummy nodes simplify linked list problems.
- How to create a new linked list dynamically.

✅ Problem Solved: Add Two Numbers (LeetCode #2)

🐍 Language: Python

📅 Day 2 of Daily DSA Practice
