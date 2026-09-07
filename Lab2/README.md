# Lab 2 - Loops and Number Programs

## Analysis Section (Answers for Workbook & README)

### For Loop vs. While Loop

**1. Compare the `for` loop and `while` loop approaches you used in this lab. For which programs above did you prefer `for`, and for which did you prefer `while`? Explain why in 2-3 lines.**

**Answer:** I preferred `for` loops for iteration tasks with known boundaries, such as pattern printing and finding prime, perfect, or Armstrong numbers, because they are concise and less prone to infinite loops. I preferred `while` loops for unbounded interactions, such as the menu application and number guessing game, where execution depends dynamically on user input conditions.

### Fibonacci Program Comparison

**2. For the Fibonacci program, compare the loop-based and recursive versions. Which one repeats more work as `n` grows, and why?**

**Answer:** The recursive version repeats significantly more work as `n` grows because it redundantly recomputes identical sub-problems multiple times in a binary tree structure, resulting in exponential O(2^n) time complexity. The loop-based version computes values iteratively in linear O(n) time by storing previous terms.

### Prime Number Check

**3. For the prime number check, what is the largest divisor you actually need to test up to, instead of checking all the way up to `n - 1`? Explain briefly why this works.**

**Answer:** You only need to test divisors up to the square root of `n` (√n). This works because if a number `n` can be factored into two factors (`n = a × b`), one of those factors must be less than or equal to √n; otherwise, their product would exceed `n`.

### Number Guessing Game Strategy

**4. In the Number Guessing Game, what strategy could a user follow to minimize the number of guesses, regardless of the range? Name the strategy.**

**Answer:** The optimal strategy is called Binary Search (or interval halving), where the user always guesses the exact midpoint of the remaining valid range to eliminate half of the possibilities with each turn.
