# Day 26 of My DSA Journey 🚀

## Problem 26: Find Minimum in Rotated Sorted Array

### Difficulty
Medium

### Problem Link

[LeetCode - Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

### Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times.

Given the sorted rotated array `nums` of unique elements, return the minimum element of the array.

You must write an algorithm that runs in:

```text
O(log n)
```

time.

---

## Optimized Approach (Binary Search)

- Use Binary Search to find the minimum element.
- Compare the middle element with the rightmost element.
- If the middle element is greater than the rightmost element, the minimum lies on the right side.
- Otherwise, the minimum lies on the left side including the middle element.
- Continue reducing the search space until both pointers meet.
- Return the element at the final position.

---

## Example

### Input

```text
nums = [3,4,5,1,2]
```

---

### Step 1

```text
left = 0
right = 4
```

Find middle:

```text
mid = (0 + 4) // 2 = 2
```

Middle element:

```text
nums[mid] = 5
```

Right element:

```text
nums[right] = 2
```

Compare:

```text
5 > 2
```

Minimum must be on the right side.

Move:

```text
left = mid + 1
```

Now:

```text
left = 3
right = 4
```

---

### Step 2

Find middle:

```text
mid = (3 + 4) // 2 = 3
```

Middle element:

```text
nums[mid] = 1
```

Right element:

```text
nums[right] = 2
```

Compare:

```text
1 < 2
```

Minimum may be at mid.

Move:

```text
right = mid
```

Now:

```text
left = 3
right = 3
```

---

### Step 3

Pointers meet.

Minimum element:

```text
nums[3] = 1
```

---

## Final Output

```text
1
```

---

## Explanation

The key idea is to identify which half contains the minimum element.

If the middle element is greater than the rightmost element, the minimum must be in the right half.

Otherwise, the minimum lies in the left half including the middle element.

By repeatedly eliminating half of the array, Binary Search efficiently finds the minimum element.

---

## Time Complexity

```text
O(log n)
```

Reason:

- The search space is reduced by half in every iteration.

---

## Space Complexity

```text
O(1)
```

Reason:

- Only a few variables are used.

---

## What I Learned

- How Binary Search works on rotated sorted arrays.
- How to identify which half contains the minimum element.
- Why comparing `nums[mid]` and `nums[right]` is important.
- How to eliminate half of the search space efficiently.
- Why this approach achieves O(log n) time complexity.
- How rotated sorted array problems differ from normal Binary Search problems.

---

✅ Problem Solved: Find Minimum in Rotated Sorted Array (LeetCode #153)

🐍 Language: Python

📅 Day 26 of Daily DSA Practice
