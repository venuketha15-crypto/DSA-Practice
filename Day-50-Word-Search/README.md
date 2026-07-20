# Day 50 of My DSA Journey 🚀

## Problem 50: Word Search

### Difficulty
Medium

### Problem Link

[LeetCode - Word Search](https://leetcode.com/problems/word-search/)

### Problem Statement

Given an `m × n` board of characters and a string `word`, return `True` if the word exists in the board.

The word must be formed using letters from adjacent cells.

We can move:

- Up
- Down
- Left
- Right

The same cell cannot be used more than once while forming the word.

---

## Optimized Approach (DFS + Backtracking)

- Traverse every cell of the board to find a possible starting point.
- Start DFS only when the current cell matches the first character of the word.
- Check whether the current cell matches the character we are searching for.
- Temporarily mark the matched cell as visited.
- Search for the next character in four directions: down, up, right, and left.
- If a path does not work, go back and try another direction.
- Restore the visited cell to its original character after searching.
- If all characters of the word are matched, return `True`.
- If no starting point can form the complete word, return `False`.

---

## Example

### Input

```text
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word = "ABCCED"
```

Board:

```text
A B C E
S F C S
A D E E
```

---

### Step 1: Find a Starting Point

The first character of the word is:

```text
word[0] = A
```

We traverse the board looking for `A`.

The first cell is:

```text
board[0][0] = A
```

It matches the first character.

So we start DFS:

```text
dfs(0, 0, 0)
```

Here:

```text
r = 0       → Current row
c = 0       → Current column
index = 0   → Character we are currently searching for
```

---

### Step 2: Match `A`

Current cell:

```text
board[0][0] = A
word[0] = A
```

They match.

Before searching for the next character, temporarily mark `A` as visited:

```text
# B C E
S F C S
A D E E
```

Now search for:

```text
word[1] = B
```

in the four neighboring directions.

---

### Step 3: Find `B`

From `A`, the right cell is:

```text
board[0][1] = B
```

It matches:

```text
word[1] = B
```

So the path becomes:

```text
A → B
```

Mark `B` as visited and search for:

```text
word[2] = C
```

---

### Step 4: Find the First `C`

From `B`, move right:

```text
board[0][2] = C
```

It matches:

```text
word[2] = C
```

Path:

```text
A → B → C
```

Now search for:

```text
word[3] = C
```

---

### Step 5: Find the Second `C`

From the first `C`, move down:

```text
board[1][2] = C
```

It matches the next character.

Path:

```text
A → B → C
        ↓
        C
```

Now search for:

```text
word[4] = E
```

---

### Step 6: Find `E`

Move down:

```text
board[2][2] = E
```

It matches.

Path:

```text
A → B → C
        ↓
        C
        ↓
        E
```

Now search for:

```text
word[5] = D
```

---

### Step 7: Find `D`

From `E`, move left:

```text
board[2][1] = D
```

It matches.

The complete path is:

```text
A → B → C
        ↓
        C
        ↓
D ← E
```

We formed:

```text
A → B → C → C → E → D
```

which is:

```text
ABCCED
```

---

### Step 8: Entire Word Matched

The word contains 6 characters.

```text
A B C C E D
0 1 2 3 4 5
```

After matching `D`, the next index becomes:

```text
index = 6
```

Since:

```text
index == len(word)

6 == 6
```

the complete word has been found.

So DFS returns:

```text
True
```

---

### Step 9: Backtracking and Restoring Cells

While searching, matched cells were temporarily marked as visited.

After the search, each cell is restored to its original character.

The restoration happens while the recursive calls return:

```text
Word completed → True
        ↓
Restore D → return True
        ↓
Restore E → return True
        ↓
Restore C → return True
        ↓
Restore C → return True
        ↓
Restore B → return True
        ↓
Restore A → return True
```

This process of:

```text
Choose → Explore → Restore
```

is called **Backtracking**.

The original board remains unchanged after the search.

---

## Final Output

```python
True
```

---

## Explanation

The solution has two main parts:

### 1. For Loops – Find Starting Points

The two loops traverse every cell of the board.

Their job is only to find a possible starting point.

```text
For Loops
    ↓
Find a cell matching word[0]
    ↓
Start DFS
```

For example:

```text
word = "ABCCED"

First character = A
```

When the loop finds:

```text
board[0][0] = A
```

DFS starts from that position.

If DFS returns `False`, the loops continue searching for another possible starting point.

If DFS returns `True`, we immediately return `True` and stop.

---

### 2. DFS – Find the Complete Word

Once a starting point is found, DFS searches for the remaining characters.

From every matched cell, it can search:

```text
        Up
         ↑
Left ← Cell → Right
         ↓
       Down
```

For every valid character:

```text
Match
  ↓
Mark as visited
  ↓
Search 4 directions
  ↓
Restore the cell
  ↓
Return True or False
```

The temporary visited mark prevents the same cell from being used twice in the same path.

After exploring, the original character is restored so that the cell can be used in another possible path.

## Time Complexity

```text
O(m × n × 4^L)
```

Where:

- `m` = number of rows.
- `n` = number of columns.
- `L` = length of the word.

Reason:

- We may consider each board cell as a possible starting point.
- During DFS, we explore neighboring cells to find the next character.
- In the worst case, multiple possible paths may need to be explored.

Overall worst-case complexity:

```text
O(m × n × 4^L)
```

---

## Space Complexity

```text
O(L)
```

Reason:

- We do not create a separate visited matrix.
- We temporarily mark visited cells directly in the board.
- The recursion stack can go as deep as the length of the word.

Therefore:

```text
O(L)
```

---

## What I Learned

- How backtracking restores cells after exploring a path.
- How `True` or `False` returns through previous recursive calls.
- The difference between the outer loops and DFS:
  - For loops → Find starting points.
  - DFS → Search for the complete word.

---

✅ Problem Solved: Word Search (LeetCode #79)

🐍 Language: Python

📅 Day 50 of Daily DSA Practice
