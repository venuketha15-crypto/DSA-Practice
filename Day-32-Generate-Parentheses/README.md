# Day 32 of My DSA Journey 🚀

## Problem 32: Generate Parentheses

### Difficulty
Medium

### Problem Link

[LeetCode - Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

### Problem Statement

Given `n` pairs of parentheses, generate all possible combinations of well-formed (valid) parentheses.

---

## Optimized Approach (Recursion + Backtracking)

- Use recursion to build the parentheses one character at a time.
- Keep track of the number of opening and closing brackets used.
- Add `"("` only if the number of opening brackets used is less than `n`.
- Add `")"` only if the number of closing brackets used is less than the number of opening brackets.
- Once both opening and closing brackets reach `n`, store the current valid combination.
- After each recursive call, remove the last added bracket (`stack.pop()`) to explore other possible combinations.

---

## Example

### Input

```text
n = 3
```

---

### Step 1

Start with an empty string.

```text
""
```

Add `"("`

```text
(
```

---

### Step 2

Add another `"("`

```text
((
```

---

### Step 3

Add another `"("`

```text
(((
```

Now all opening brackets are used.

---

### Step 4

Add closing brackets.

```text
((()
```

```text
((())
```

```text
((()))
```

Store this valid combination.

---

### Step 5

Backtrack by removing the last bracket and explore other choices.

Generate:

```text
(()())
```

```text
(())()
```

```text
()(())
```

```text
()()()
```

---

## Final Output

```text
[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]
```

---

## Explanation

This problem is solved using **Recursion + Backtracking**.

At every step, we have at most two choices:

- Add `"("`
- Add `")"`

We must follow these rules:

```text
1. open < n
2. close < open
```

These rules ensure that only valid parentheses combinations are generated.

After exploring one choice, `stack.pop()` removes the last bracket so that recursion can explore the next possible choice. This process is called **backtracking**.

---

## Time Complexity

```text
O(4ⁿ / √n)
```

Reason:

- The algorithm generates **all valid parentheses combinations**.
- The number of valid combinations follows the **Catalan Numbers**.
- The nth Catalan Number grows approximately as:

```text
4ⁿ / √n
```

Since every valid combination must be generated, the overall time complexity is:

```text
O(4ⁿ / √n)
```

---

## Space Complexity

```text
O(n)
```

Reason:

- The recursion call stack and temporary stack together store at most `2 × n` characters.
- Excluding the output list, the auxiliary space complexity is `O(n)`.

---

## What I Learned

- How recursion builds solutions step by step.
- How backtracking explores all possible valid combinations.
- Why we use a stack to build the current parentheses string.
- Why `stack.pop()` is used to undo the previous choice.
- How recursion and backtracking work together.
- Why the number of valid combinations follows the Catalan Numbers.
- Why the optimized solution has a time complexity of **O(4ⁿ / √n)**.

---

✅ Problem Solved: Generate Parentheses (LeetCode #22)

🐍 Language: Python

📅 Day 32 of Daily DSA Practice
```
