# Understand Time and Space Complexity
### A Complete Beginner-to-Intermediate Guide

---

## Table of Contents
1. [What is Time Complexity?](#1-what-is-time-complexity)
2. [Big O Notation](#2-big-o-notation)
3. [All Complexity Classes Explained](#3-all-complexity-classes-explained)
4. [Rules for Calculating Time Complexity](#4-rules-for-calculating-time-complexity)
5. [Big O, Omega, and Theta](#5-big-o-omega-and-theta)
6. [Space Complexity](#6-space-complexity)
7. [TLE — Time Limit Exceeded](#7-tle--time-limit-exceeded)
8. [Python Data Structure Complexities](#8-python-data-structure-complexities)
9. [Quick Reference Cheat Sheet](#9-quick-reference-cheat-sheet)

---

## 1. What is Time Complexity?

When you write code, two questions matter most:

1. **Does it give the correct answer?**
2. **Is it fast enough?**

Time Complexity answers question 2 — but not by measuring seconds on a stopwatch.

### The Real Question

> "As input gets bigger, how much more work does the program do?"

This is important because the same code runs faster on a powerful computer and slower on a weak one. Measuring actual seconds is unreliable. Instead, we count **how many operations the algorithm performs** relative to the input size `N`.

### A Simple Example

```
Searching through 10 names in a list → maybe 10 comparisons.
Searching through 1,000,000 names   → maybe 1,000,000 comparisons.
```

The work grew **proportionally** with N. That's linear time — and that's what Time Complexity captures.

---

## 2. Big O Notation

**Big O Notation** is the standard way to write Time Complexity.

It is written as: `O(expression)`

The expression describes how the number of operations grows as N increases.

### What Big O Tells You
- It describes the **worst-case scenario**.
- It ignores small details (constants, minor terms) to show the **big picture**.
- It is machine-independent — valid everywhere.

### Why Ignore Constants?

```
O(3N) and O(N) both grow linearly.
At N = 1,000,000, whether it's 1× or 3× doesn't change the shape of the growth.
So O(3N) is simplified to O(N).
```

---

## 3. All Complexity Classes Explained

From **fastest** (most efficient) to **slowest** (least efficient):

---

### O(1) — Constant Time

No matter how large N gets, the operation always takes the **same number of steps**.

**Example:** Getting an element from an array by its index.

```python
arr = [10, 20, 30, 40, 50]
print(arr[2])  # Always 1 step, regardless of array size → O(1)
```

**Real-world analogy:** Opening a book directly to page 42. It doesn't matter how thick the book is.

---

### O(log N) — Logarithmic Time

The number of steps grows **very slowly** — the input is cut in half each time.

**Example:** Binary Search (searching a sorted list by repeatedly halving the search space).

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**Key fact:** For N = 1,000,000, binary search takes only about **20 steps**.

**Real-world analogy:** Finding a word in a dictionary by opening the middle, then deciding left or right, and repeating.

---

### O(N) — Linear Time

The number of steps grows **directly proportional** to N.

**Example:** Reading every element once, like a linear search.

```python
def find_item(arr, target):
    for item in arr:      # Visits every element once
        if item == target:
            return True
    return False
```

**Real-world analogy:** Finding someone's name on an unsorted list by reading from top to bottom.

---

### O(N log N) — Linearithmic Time

Slightly worse than O(N), much better than O(N²). This is the complexity of the best sorting algorithms.

**Example:** Merge Sort, Python's built-in `sort()`.

```python
arr.sort()  # Uses Timsort → O(N log N)
```

**Real-world analogy:** Sorting a shuffled deck by splitting it in half repeatedly and merging the halves in order.

---

### O(N²) — Quadratic Time

Usually caused by a **loop inside a loop**. Work grows as the square of N.

**Example:** Bubble Sort — comparing every element against every other element.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # Outer loop: runs N times
        for j in range(n - 1):  # Inner loop: runs N times
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# Total operations ≈ N × N = N²
```

**Warning:** At N = 100,000, this means 10 billion operations. That's too slow.

---

### O(N³) — Cubic Time

Three nested loops. Grows even faster than O(N²).

**Example:** Naive matrix multiplication.

Only practical for very small inputs (N ≤ 500 or so).

---

### O(2^N) — Exponential Time

Work **doubles** with every additional element. Gets out of hand very quickly.

**Example:** Generating all possible subsets of a set.

```python
def all_subsets(arr):
    if not arr:
        return [[]]
    rest = all_subsets(arr[1:])
    return rest + [[arr[0]] + s for s in rest]
# For N = 30, this runs over 1 billion times.
```

Only usable for very small N (N ≤ 20–25).

---

### Complexity Growth at a Glance

| N | O(1) | O(log N) | O(N) | O(N log N) | O(N²) | O(2^N) |
|---|------|----------|------|------------|--------|--------|
| 10 | 1 | 3 | 10 | 33 | 100 | 1,024 |
| 100 | 1 | 7 | 100 | 664 | 10,000 | 10^30 |
| 1,000 | 1 | 10 | 1,000 | 10,000 | 1,000,000 | 10^301 |

**Takeaway:** The complexity class matters far more than the constant factor.

---

## 4. Rules for Calculating Time Complexity

When analyzing an algorithm, follow these three rules every time.

---

### Rule 1: Always Consider the Worst Case

You want to know how bad things can get, not how good.

```
Linear search for a target that doesn't exist → looks at all N elements → O(N)
Even if target is sometimes at index 0 (O(1)), we report O(N) for safety.
```

---

### Rule 2: Drop Constants

Constant multipliers don't change the growth pattern.

```
O(2N)    →  O(N)
O(5N²)   →  O(N²)
O(1000)  →  O(1)
O(N/2)   →  O(N)
```

---

### Rule 3: Drop Lower-Order Terms

When you have multiple terms, keep only the one that grows fastest.

```
O(N² + N)           →  O(N²)
O(N³ + N² + N + 1)  →  O(N³)
O(N + log N)        →  O(N)
O(2^N + N¹⁰⁰)      →  O(2^N)
```

**Why?** At large N, the dominant term completely overshadows the rest. For N = 1,000,000: N² = 10^12, while N = 10^6. N is only 0.0001% of the total — it simply doesn't matter.

---

### Worked Example: Combining All Three Rules

```python
def example(arr):
    x = arr[0]                        # 1 operation → O(1)

    for i in range(len(arr)):         # N operations → O(N)
        print(arr[i])

    for i in range(len(arr)):         # N × N operations → O(N²)
        for j in range(len(arr)):
            print(arr[i] + arr[j])
```

**Step-by-step:**
1. Add up all parts: `O(1) + O(N) + O(N²)`
2. Apply Rule 3 (drop lower-order terms): keep only `O(N²)`
3. **Final answer: O(N²)**

---

## 5. Big O, Omega, and Theta

There are three formal notations, each describing a different "bound" on an algorithm's behavior.

---

### Big O (O) — Worst Case / Upper Bound

The algorithm will **never perform worse** than this.

Think of it as the **ceiling**.

> Linear Search: O(N) — in the worst case, we check all N elements.

---

### Omega (Ω) — Best Case / Lower Bound

The algorithm will **never perform better** than this.

Think of it as the **floor**.

> Linear Search: Ω(1) — in the best case, the target is at index 0.

---

### Theta (Θ) — Average Case / Tight Bound

The algorithm is **exactly** this complex — the upper and lower bounds are the same.

Think of it as the **exact fit**.

> Merge Sort: Θ(N log N) — it always takes N log N steps, regardless of input.

---

### Summary Table

| Notation | Full Name | Meaning | Mental Image |
|----------|-----------|---------|--------------|
| O(f(N)) | Big O | Worst Case | Ceiling |
| Ω(f(N)) | Omega | Best Case | Floor |
| Θ(f(N)) | Theta | Exact / Average | Exact fit |

**In practice:** When people say "the time complexity is O(N)", they almost always mean Big O (worst case). This is the standard in both interviews and competitive programming.

---

## 6. Space Complexity

Space Complexity measures how much **memory** an algorithm uses.

### The Formula

```
Space Complexity = Input Space + Auxiliary Space
```

### Input Space
Memory needed to **store the input itself**.

> An array of N integers → O(N) input space.

This is usually **not counted** when reporting space complexity, since the input has to exist regardless.

### Auxiliary Space
The **extra memory** the algorithm creates while running.

This is what matters most.

---

### Examples of Different Auxiliary Spaces

**O(1) Auxiliary Space — No extra memory used:**
```python
def find_max(arr):
    max_val = arr[0]     # Just one variable — constant extra space
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val
```

**O(N) Auxiliary Space — New structure created:**
```python
def get_doubled(arr):
    result = []           # A new list of size N is created
    for x in arr:
        result.append(x * 2)
    return result
```

**O(N) Space from Recursion — Call stack grows:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # N function calls sit on the stack at once
```

---

### The Space-Time Tradeoff

Using more memory can often make code faster.

> **Example:** Memoization stores previously computed results in a dictionary.
> This uses O(N) extra space but reduces time from O(2^N) to O(N).

This tradeoff is one of the most important concepts in algorithm design.

---

## 7. TLE — Time Limit Exceeded

### What Is TLE?

On competitive programming platforms (LeetCode, Codeforces, HackerRank, etc.), your code must run within a time limit — usually 1 to 2 seconds.

If your code takes too long, the judge returns:

```
Time Limit Exceeded (TLE)
```

**Important insight:** TLE usually means your **logic is correct** but your **algorithm is too slow**.

---

### The Golden Rule

```
1 second ≈ 10^8 operations
```

This is the standard estimate used across competitive programming.

---

### How to Predict TLE Before Submitting

**Formula:**
```
Estimated time (seconds) = Total operations / 10^8
```

**Example — Will this pass?**
- Input constraint: N = 100,000 (10^5)
- Your algorithm: O(N²)
- Total operations: (10^5)² = 10^10
- Estimated time: 10^10 / 10^8 = **100 seconds**
- Result: **TLE ❌**

**Fixed version using O(N log N):**
- Operations: 10^5 × log₂(10^5) ≈ 10^5 × 17 ≈ 1,700,000
- Estimated time: 1,700,000 / 10^8 ≈ **0.017 seconds**
- Result: **Accepted ✅**

---

### Constraint → Required Complexity Table

Use this table when reading a problem's constraints:

| Input Size (N) | Safe Complexity | Example Algorithms |
|----------------|----------------|--------------------|
| N ≤ 10 | O(N!) or O(2^N) | Brute force, permutations |
| N ≤ 20 | O(2^N) | Subset enumeration, bitmask DP |
| N ≤ 500 | O(N³) | Floyd-Warshall, naive DP |
| N ≤ 5,000 | O(N²) | Bubble/Selection Sort, O(N²) DP |
| N ≤ 10^6 | O(N log N) | Merge Sort, Heap Sort |
| N ≤ 10^7 | O(N) | Two Pointers, Hashing |
| N ≤ 10^9 | O(log N) | Binary Search |
| Any N | O(1) | Direct formula |

---

### TLE Fixing Strategy

If your O(N²) solution gets TLE, ask yourself:

```
Can I sort first, then binary search?       → O(N log N)
Can I use a hash map to store results?      → O(N)
Can I use two pointers?                     → O(N)
Can I precompute prefix sums?               → O(N) build, O(1) query
```

Each step up this ladder often requires a completely different approach.

---

## 8. Python Data Structure Complexities

Python's built-in structures have different performance characteristics. Knowing these helps you write faster code automatically.

---

### List

A **dynamic array**. Fast at the ends, slow in the middle.

| Operation | Complexity | Reason |
|-----------|-----------|--------|
| `arr[i]` — index access | O(1) | Direct memory address |
| `arr[i] = x` — update | O(1) | Direct memory write |
| `arr.append(x)` | O(1) amortized | Adds to the end |
| `arr.pop()` — remove last | O(1) | Removes from end |
| `arr.pop(i)` — remove middle | O(N) | Everything after must shift left |
| `arr.insert(i, x)` | O(N) | Everything after must shift right |
| `del arr[i]` | O(N) | Everything after must shift |
| `x in arr` — search | O(N) | Scans every element |
| `min(arr)` / `max(arr)` | O(N) | Scans every element |
| `len(arr)` | O(1) | Stored internally |
| `arr.sort()` | O(N log N) | Timsort algorithm |
| `arr[a:b]` — slice | O(K) | K = number of elements sliced |
| `arr[:]` — full copy | O(N) | Copies all N elements |
| Iterate | O(N) | Visits every element |

**Common mistake to avoid:**

```python
# SLOW — O(N²) total
for item in data:
    my_list.insert(0, item)   # Each insert shifts everything → O(N) per call

# FAST — O(N) total
for item in data:
    my_list.append(item)      # O(1) each
my_list.reverse()             # O(N) once at the end
```

---

### Set

A **hash table** storing unique values. No duplicates, no guaranteed order.

| Operation | Average Case | Worst Case |
|-----------|-------------|-----------|
| `x in s` — check membership | O(1) | O(N) |
| `s.add(x)` | O(1) | O(N) |
| `s.remove(x)` | O(1) | O(N) |
| `s.discard(x)` | O(1) | O(N) |
| Iterate | O(N) | O(N) |
| `s1 \| s2` — union | O(len(s1) + len(s2)) | — |
| `s1 & s2` — intersection | O(min(len(s1), len(s2))) | — |

**Why worst case is O(N):** Hash collisions. When two different values produce the same hash, they pile up in the same bucket and must be searched linearly. This is rare in practice.

**Best use cases:**
- Fast membership checking: `if x in my_set` is O(1), not O(N)
- Removing duplicates from a list: `unique = list(set(arr))`
- Storing "visited" elements in graph problems

```python
# SLOW — list membership check is O(N)
visited = []
if node not in visited:   # O(N) scan
    visited.append(node)

# FAST — set membership check is O(1)
visited = set()
if node not in visited:   # O(1) hash check
    visited.add(node)
```

---

### Dictionary

A **hash table** storing key-value pairs. Extremely powerful for mapping and counting.

| Operation | Average Case | Worst Case |
|-----------|-------------|-----------|
| `d[key]` — get value | O(1) | O(N) |
| `d[key] = val` — insert/update | O(1) | O(N) |
| `del d[key]` — delete | O(1) | O(N) |
| `key in d` — check key | O(1) | O(N) |
| `d.copy()` | O(N) | O(N) |
| Iterate `d.items()` | O(N) | O(N) |

**Best use cases:**
- Counting frequencies
- Mapping values to other values
- Caching computed results (memoization)

```python
# Counting character frequency — O(N)
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Two Sum — O(N) with a dictionary
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:       # O(1) lookup instead of O(N) scan
            return [seen[complement], i]
        seen[num] = i
```

---

### Quick Comparison: List vs Set vs Dict

| Task | Best Structure | Why |
|------|---------------|-----|
| Store ordered data | List | Maintains insertion order |
| Check if value exists | Set | O(1) lookup |
| Map key → value | Dict | O(1) access by key |
| Count occurrences | Dict | Fast insertion and update |
| Remove duplicates | Set | Auto-deduplication |
| Sort data | List | Only lists have `.sort()` |

---

## 9. Quick Reference Cheat Sheet

### The Three Rules

```
1. Always consider the WORST CASE
2. DROP constants         →  O(5N) = O(N)
3. DROP lower-order terms →  O(N² + N) = O(N²)
```

---

### Complexity Order (Best → Worst)

```
O(1) → O(log N) → O(N) → O(N log N) → O(N²) → O(N³) → O(2^N) → O(N!)
```

---

### TLE Rule

```
10^8 operations ≈ 1 second
```

---

### Big O / Omega / Theta

| Notation | Case | Think of it as |
|----------|------|---------------|
| O | Worst | Ceiling |
| Ω | Best | Floor |
| Θ | Exact / Average | Both ceiling and floor |

---

### Space Complexity

```
Space = Input Space + Auxiliary Space
What matters in interviews → Auxiliary Space (extra memory you create)
```

---

### Python List: Fast vs Slow Operations

| Fast — O(1) | Slow — O(N) |
|-------------|------------|
| `arr[i]` | `arr.insert(i, x)` |
| `arr.append(x)` | `arr.pop(i)` |
| `arr.pop()` | `x in arr` |
| `len(arr)` | `min(arr)`, `max(arr)` |

---

### Python Set: All Core Operations = O(1) Average

```
Membership check  →  O(1)
Add element       →  O(1)
Remove element    →  O(1)
```

---

### Python Dict: All Core Operations = O(1) Average

```
Read value        →  O(1)
Insert/Update     →  O(1)
Delete            →  O(1)
Key membership    →  O(1)
```

---

### Constraint → Complexity Quick Reference

```
N ≤ 10          →  O(2^N) or O(N!) is okay
N ≤ 500         →  O(N³) is okay
N ≤ 5,000       →  O(N²) is okay
N ≤ 1,000,000   →  O(N log N) needed
N ≤ 10,000,000  →  O(N) needed
N ≤ 1,000,000,000 →  O(log N) needed
```

---

*A complete foundation guide to Time and Space Complexity — from basics to practical application.*
