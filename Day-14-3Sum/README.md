# Day 14 of My DSA Journey 🚀

## Problem 14: 3Sum

### Difficulty
Medium

### Problem Link

[LeetCode - 3Sum](https://leetcode.com/problems/3sum/)

### Problem Statement

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

### Approach (Sorting + Two Pointers)

- Sort the array first.
- Fix one element using index `i`.
- Skip duplicate values for `i`.
- Use two pointers:
  - `left` starts from `i + 1`.
  - `right` starts from the end of the array.
- Calculate the sum of the three elements.
- If the sum is zero:
  - Add the triplet to the result.
  - Move both pointers inward.
  - Skip duplicate values.
- If the sum is less than zero, move `left` to increase the sum.
- If the sum is greater than zero, move `right` to decrease the sum.
- Continue until `left` and `right` meet.

### Example

Input:

```text
nums = [-1,0,1,2,-1,-4]
```

After sorting:

```text
[-4,-1,-1,0,1,2]
```

### Step 1

Fix:

```text
i = 0
nums[i] = -4
```

```text
left = 1
right = 5
```

Calculate:

```text
-4 + (-1) + 2 = -3
```

Since the sum is less than zero, move `left`.

No triplet found.

---

### Step 2

Fix:

```text
i = 1
nums[i] = -1
```

```text
left = 2
right = 5
```

Calculate:

```text
-1 + (-1) + 2 = 0
```

Triplet found:

```text
[-1,-1,2]
```

Move both pointers inward.

---

### Step 3

Now:

```text
left = 3
right = 4
```

Calculate:

```text
-1 + 0 + 1 = 0
```

Triplet found:

```text
[-1,0,1]
```

Move both pointers inward.

---

Skip duplicate values and continue.

### Final Result

```text
[[-1,-1,2],[-1,0,1]]
```

Output:

```text
[[-1,-1,2],[-1,0,1]]
```

### Explanation

The key idea is to sort the array first.

After fixing one element, we use two pointers to search for the remaining two elements whose sum equals the negative of the fixed element.

Sorting helps us:

- Efficiently move pointers.
- Avoid duplicate triplets.
- Solve the problem in quadratic time.

For:

```text
[-1,0,1,2,-1,-4]
```

The unique triplets whose sum equals zero are:

```text
[-1,-1,2]
[-1,0,1]
```

### Time Complexity

O(n²)

- Sorting takes O(n log n).
- The outer loop runs O(n) times.
- The two pointers together traverse the remaining array in O(n).

Overall Time Complexity:

```text
O(n²)
```

### Space Complexity

O(k)

where `k` is the number of unique triplets stored in the result.

Ignoring the output array, the extra space used is O(1).

### What I Learned

- How to solve 3Sum using Sorting and Two Pointers.
- Why sorting helps eliminate duplicates.
- How to skip duplicate values efficiently.
- How to use a fixed element with two moving pointers.
- Why 3Sum is one of the most important Two Pointers interview problems.
- How to solve a Medium problem in O(n²) time.

✅ Problem Solved: 3Sum (LeetCode #15)

🐍 Language: Python

📅 Day 14 of Daily DSA Practice
