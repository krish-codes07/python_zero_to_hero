# Chapter 10 – Functions

## Overview
This chapter covers functions in Python — how to define them, pass data in, get data out, and use advanced argument types like `*args` and `**kwargs`.

---

## Concepts Learned

- Defining functions with `def`
- Parameters and return values
- `print` vs `return` — key difference
- Default parameters
- Keyword arguments
- `*args` — variable positional arguments
- `**kwargs` — variable keyword arguments
- Unpacking lists with `*` and dicts with `**` when calling functions

---

## Files

- `basic_function.py`
- `return_vs_print.py`
- `default_parameters.py`
- `keyword_arguments.py`
- `args_demo.py`
- `kwargs_demo.py`
- `practice.py`

---

## Common Mistakes

- Using `print` inside a function instead of `return`
- Putting default parameters before non-default ones
- Passing a list to `*args` without unpacking it with `*`
- Using variables from outside the function inside it
- Forgetting that `*args` gives a tuple and `**kwargs` gives a dictionary

---

## Key Concepts at a Glance

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default parameter
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# Keyword arguments
book_ticket(meal="veg", name="Rahul", destination="Delhi")

# *args — collect any number of positional arguments
def total(*args):
    return sum(args)

total(100, 200, 300)       # args = (100, 200, 300)

# **kwargs — collect any number of named arguments
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

profile(age=20, city="Delhi")   # kwargs = {'age': 20, 'city': 'Delhi'}

# Unpacking when calling
my_list = [100, 200, 300]
total(*my_list)            # * unpacks list into *args

my_dict = {"age": 20, "city": "Delhi"}
profile(**my_dict)         # ** unpacks dict into **kwargs
```

---

## `*args` vs `**kwargs` — Quick Reference

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Type of arguments | Positional | Named (keyword) |
| Stored as | Tuple | Dictionary |
| Access | Loop with `for x in args` | Loop with `for k, v in kwargs.items()` |
| Unpack when calling | `func(*my_list)` | `func(**my_dict)` |

---

## Key Takeaway

Functions are the foundation of clean, reusable Python code. Every freelance script, web scraper, and automation tool is built on well-structured functions. Mastering `*args` and `**kwargs` gives you the flexibility to build tools that work for any input.