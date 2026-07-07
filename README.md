# Pytest Parameterized Testing  
**Doing more tests with less code**  
_By Bill Shpelak_

---

## 📌 Overview

This README introduces **pytest parameterization**, a powerful technique that lets you test multiple input/output combinations using **one test function** instead of many repetitive ones.

You’ll see:

- Why traditional tests become repetitive  
- How parameterization reduces boilerplate  
- Why loops inside tests are misleading  
- How pytest gives clearer, more maintainable failures  

---

## 🧮 Basic Functions to Test

```python
def add(a, b):
    """Add two numbers together."""
    return a + b
```

```python
def add_wrong(a, b):
    """Add two numbers together, but with a bug."""
    return abs(a) + b
```

---

## ❌ Traditional Testing (Too Much Code)

```python
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5

def test_add_float_and_integer():
    assert add(2.5, 3) == 5.5

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000

def test_add_negative_and_positive():
    assert add(-2, 3) == 1
```

This works… but it’s **repetitive**, **harder to maintain**, and **scales poorly**.

---

# ✅ Pytest Parameterization

```python
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 5, 5),
        (2.5, 3, 5.5),
        (1_000_000, 2_000_000, 3_000_000),
        (-2, 3, 1),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### 🎯 Benefits

- **Code Reusability** — one test, many cases  
- **Improved Readability** — test data is visible and organized  
- **Efficiency** — fewer lines, same coverage  
- **Scalability** — add more cases easily  
- **Better Maintenance** — failures are isolated and descriptive  

---

# ⚠️ Why Not Use a For Loop?

```python
test_cases = [
    (2, 3, 5),
    (-2, -3, -5),
    (0, 5, 5),
    (2.5, 3, 5.5),
    (1_000_000, 2_000_000, 3_000_000),
    (-2, 3, 1),
]

def test_add_wrong():
    for a, b, expected in test_cases:
        assert add_wrong(a, b) == expected

    # Extra assertion
    assert -1 == -5  # where -1 = add_wrong(-2, -3)
```

### ❗ Problem

Pytest reports **only one failure**, and it’s not tied to a specific test case:

```
FAILED test_add_wrong - assert -1 == -5
```

You lose:

- Which input caused the failure  
- Which iteration failed  
- Clear debugging context  

---

# 🎉 Parameterization Fixes This

Each test case becomes its **own test**, with its own name:

```
test_add_wrong[-2--3--1]
test_add_wrong[2--3--5]
...
```

Example:

```python
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 5, 5),
        (2.5, 3, 5.5),
        (1_000_000, 2_000_000, 3_000_000),
        (-2, 3, 1),
    ],
)
def test_add_wrong(a, b, expected):
    assert add_wrong(a, b) == expected
```

### 🔍 Clear Failure Output

```
FAILED test_add_wrong[-2--3--5] - assert -1 == -5
FAILED test_add_wrong[-2-3-1] - assert 5 == 1
```

You instantly know:

- Which inputs failed  
- What the function returned  
- What was expected  

This is the power of pytest parameterization.

---

## 📘 Summary

Pytest parameterization:

- Makes tests **cleaner**
- Makes failures **more informative**
- Makes your test suite **more scalable**
- Prevents misleading loop-based failures

If you're writing multiple similar tests, parameterization is almost always the better choice.

---