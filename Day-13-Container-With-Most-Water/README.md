# Day 13 of My DSA Journey 🚀

## Problem 13: Container With Most Water

### Difficulty
Medium

### Problem Link

[LeetCode - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

### Problem Statement

You are given an integer array `height` of length `n`.

There are `n` vertical lines drawn such that the two endpoints of the `iᵗʰ` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds the maximum amount of water.

Return the maximum amount of water a container can store.

### Optimized Approach (Two Pointers)

- Use two pointers:
  - `left` starts from the beginning of the array.
  - `right` starts from the end of the array.
- Calculate the area formed by the two lines.
- Update the maximum area if the current area is larger.
- Move the pointer with the smaller height inward.
- Continue until the two pointers meet.

### Example

Input:

```text
height = [1,8,6,2,5,4,8,3,7]
```

Initial:

```text
left = 0
right = 8
max_area = 0
```

### Step 1

Compare:

```text
height[left] = 1
height[right] = 7
```

Height:

```text
min(1, 7) = 1
```

Width:

```text
8 - 0 = 8
```

Area:

```text
1 × 8 = 8
```

Update:

```text
max_area = 8
```

Move the smaller height:

```text
left += 1
```

---

### Step 2

```text
left = 1
right = 8
```

Compare:

```text
height[left] = 8
height[right] = 7
```

Height:

```text
min(8, 7) = 7
```

Width:

```text
8 - 1 = 7
```

Area:

```text
7 × 7 = 49
```

Update:

```text
max_area = 49
```

Move the smaller height:

```text
right -= 1
```

---

### Step 3

```text
left = 1
right = 7
```

Area:

```text
min(8, 3) × (7 - 1)
= 3 × 6
= 18
```

```text
max_area = 49
```

Move:

```text
right -= 1
```

---

Continue the same process until:

```text
left >= right
```

### Final Result

```text
49
```

Output:

```text
49
```

### Explanation

The amount of water stored depends on:

```text
Area = Minimum Height × Width
```

The width decreases as the pointers move inward.

To have a chance of finding a larger area, we move the pointer with the smaller height because moving the taller one cannot increase the height of the container.

For:

```text
height = [1,8,6,2,5,4,8,3,7]
```

The maximum water that can be stored is:

```text
49
```

using the lines with heights:

```text
8 and 7
```

### Time Complexity

O(n)

Each pointer moves at most once across the array.

### Space Complexity

O(1)

Only a few variables are used.

### What I Learned

- How the Two Pointers technique works.
- How to calculate area using height and width.
- Why moving the smaller pointer is the optimal choice.
- How to solve a Medium problem in linear time.
- How to optimize a problem without using extra space.

✅ Problem Solved: Container With Most Water (LeetCode #11)

🐍 Language: Python

📅 Day 13 of Daily DSA Practice
