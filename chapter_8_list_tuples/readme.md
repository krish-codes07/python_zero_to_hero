# Chapter 8 – Lists and Tuples

## Overview
This chapter focuses on understanding Python lists and tuples, two important sequence data structures. These are fundamental for problem solving and form the base for Data Structures & Algorithms (DSA).

---

## Topics Covered

### 1. Lists
- Creating lists
- Indexing and negative indexing
- Slicing
- Mutability (lists are mutable)
- Updating elements
- Looping through lists
- Common list methods:
  - append()
  - insert()
  - remove()
  - pop()
  - len()

### 2. Tuples
- Creating tuples
- Tuple indexing and slicing
- Immutability (tuples cannot be modified)
- When to use tuples instead of lists

---

## Key Differences Between Lists and Tuples

| Feature | List | Tuple |
|----------|--------|---------|
| Syntax | [] | () |
| Mutable | Yes | No |
| Ordered | Yes | Yes |
| Allows duplicates | Yes | Yes |
| Performance | Slightly slower | Slightly faster |

---

## Important Concepts Learned

- Lists are mutable and can be modified.
- Tuples are immutable and cannot be changed after creation.
- Indexing starts from 0.
- Negative indexing accesses elements from the end.
- Slicing works the same way as in strings.
- pop() removes and returns the last element by default.
- Lists are heavily used in DSA as arrays.

---

## Common Mistakes

- Trying to modify a tuple.
- Confusing remove() and pop().
- Forgetting that pop() returns a value.
- Using incorrect index ranges while slicing.

---

## Practical Applications

- Storing multiple values.
- Iterating over collections.
- Implementing stacks and queues.
- Handling structured data.
- Building algorithms.

---

## Key Takeaway

Lists and tuples are core sequence data structures in Python.  
Understanding their behavior, especially mutability and indexing, is essential before moving into advanced data structures and algorithms.