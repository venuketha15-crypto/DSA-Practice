# Day 23 of My DSA Journey 🚀

## Problem 23: Best Time to Buy and Sell Stock

### Difficulty
Easy

### Problem Link

[LeetCode - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### Problem Statement

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve.

If no profit can be achieved, return `0`.

---

## Optimized Approach (Two Pointers)

- Use two pointers:
  - Left pointer represents the buying day.
  - Right pointer represents the selling day.
- Compare buying and selling prices.
- If selling price is greater than buying price, calculate profit.
- Update the maximum profit found so far.
- If a lower buying price is found, move the buying pointer to that day.
- Continue until all days are processed.

---

## Example

### Input

```text
prices = [7,1,5,3,6,4]
```

---

### Step 1

Buy Price:

```text
7
```

Sell Price:

```text
1
```

Profit:

```text
1 - 7 = -6
```

Not profitable.

Move buy pointer to:

```text
1
```

---

### Step 2

Buy Price:

```text
1
```

Sell Price:

```text
5
```

Profit:

```text
5 - 1 = 4
```

Maximum Profit:

```text
4
```

---

### Step 3

Buy Price:

```text
1
```

Sell Price:

```text
3
```

Profit:

```text
3 - 1 = 2
```

Maximum Profit remains:

```text
4
```

---

### Step 4

Buy Price:

```text
1
```

Sell Price:

```text
6
```

Profit:

```text
6 - 1 = 5
```

Maximum Profit:

```text
5
```

---

### Step 5

Buy Price:

```text
1
```

Sell Price:

```text
4
```

Profit:

```text
4 - 1 = 3
```

Maximum Profit remains:

```text
5
```

---

## Final Output

```text
5
```

---

## Explanation

The key idea is to keep track of the lowest buying price seen so far.

Whenever a higher selling price is found, calculate the profit and update the maximum profit.

If a lower buying price appears, update the buying day.

This allows us to find the maximum profit efficiently.

---

## Time Complexity

```text
O(n)
```

Where:

- `n` = length of the array.

Reason:

- Each element is visited only once.

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

- Only a few variables are used.

---

## What I Learned

- How the Two Pointer technique works.
- How to track the minimum buying price.
- How to calculate profit efficiently.
- How to update the maximum profit dynamically.
- Why this approach achieves O(n) time complexity.

---

✅ Problem Solved: Best Time to Buy and Sell Stock (LeetCode #121)

🐍 Language: Python

📅 Day 23 of Daily DSA Practice
