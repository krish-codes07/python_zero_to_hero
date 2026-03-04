# Chapter 11 – File Handling & Exception Handling

## Overview
This chapter covers how to read from and write to files in Python, and how to handle errors gracefully using exception handling — two essential skills for every real-world Python script.

---

## Part 1 — File Handling

### Concepts Learned
- Opening files with `open()`
- File modes — `"r"`, `"w"`, `"a"`, `"r+"`
- The `with` statement — why it's the professional standard
- Writing to a file with `f.write()`
- Reading a file with `f.read()`, `f.readline()`, `f.readlines()`
- Looping over a file line by line
- Using `enumerate()` for line numbering
- Using `.strip()` to clean `\n` from lines

### Files
- `write_file.py`
- `read_file.py`
- `append_file.py`
- `line_by_line.py`
- `enumerate_demo.py`
- `practice.py`

### File Modes — Quick Reference

| Mode | Action | File Exists | File Missing |
|------|--------|-------------|--------------|
| `"r"` | Read only | Opens it | ❌ Error |
| `"w"` | Write (fresh) | Overwrites | Creates new |
| `"a"` | Append | Adds to end | Creates new |
| `"r+"` | Read + Write | Opens it | ❌ Error |

### Key Concepts at a Glance

```python
# Writing to a file
with open("notes.txt", "w") as f:
    f.write("Hello World\n")       # \n moves to next line

# Reading entire file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line with line numbers
with open("notes.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")   # strip() removes \n

# Appending to a file (doesn't overwrite)
with open("notes.txt", "a") as f:
    f.write("New line added\n")
```

### Common Mistakes
- Forgetting `\n` when writing — all lines merge into one
- Using `f.readline()` inside a `for line in f` loop — skips lines
- Not using `.strip()` — causes extra blank lines in output
- Forgetting to use `with` — file may not close properly

---

## Part 2 — Exception Handling

### Concepts Learned
- Why exceptions exist — preventing program crashes
- `try` / `except` blocks
- Handling multiple exceptions
- `else` — runs only when no error occurs
- `finally` — always runs, error or not
- Common exception types

### Files
- `try_except_basic.py`
- `multiple_exceptions.py`
- `else_finally.py`
- `file_exception.py`
- `practice.py`

### Common Exception Types

| Exception | When It Happens |
|-----------|-----------------|
| `FileNotFoundError` | File doesn't exist |
| `ValueError` | Wrong type of value e.g. `int("hello")` |
| `ZeroDivisionError` | Dividing by zero |
| `TypeError` | Wrong data type used |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key doesn't exist |
| `PermissionError` | No access rights to file |

### Key Concepts at a Glance

```python
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)

except ValueError:
    print("❌ Enter numbers only!")        # wrong input type

except ZeroDivisionError:
    print("❌ Cannot divide by zero!")     # division by zero

else:
    print("✅ Calculation successful!")    # runs only if no error

finally:
    print("Calculation complete.")         # always runs
```

### Common Mistakes
- Using bare `except:` without specifying the error type
- Putting code after `return` in try block
- Forgetting `finally` for cleanup tasks
- Using `else` when you mean `finally`

---

## Key Takeaway

File handling lets your Python scripts interact with the real world — reading data, saving results, writing logs. Exception handling makes your scripts **bulletproof** — they handle errors gracefully instead of crashing. Together, these two skills are the foundation of every professional freelance script you will write.