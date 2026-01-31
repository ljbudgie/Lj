# Performance Optimization Quick Reference

## Algorithm Complexity Cheat Sheet

| Operation | Bad (O) | Good (O) | Use |
|-----------|---------|----------|-----|
| Search in list | O(n) | O(1) | Use `set` instead |
| Nested loop search | O(n²) | O(n) | Use `set.intersection()` |
| String concat in loop | O(n²) | O(n) | Use `str.join()` |
| Recursive fibonacci | O(2^n) | O(n) | Use memoization or iteration |
| Multiple list operations | O(n*k) | O(n) | Use list comprehension |
| Linear search | O(n) | O(log n) | Use binary search on sorted data |

## Data Structure Selection

```python
# Membership testing
items = set([...])           # O(1) lookup
# vs
items = [...]                # O(n) lookup

# Key-value storage
cache = {}                   # O(1) lookup
# vs
cache = [(k, v), ...]        # O(n) lookup

# FIFO queue
from collections import deque
queue = deque()              # O(1) append/popleft
# vs
queue = []                   # O(n) for pop(0)
```

## String Operations

```python
# ❌ Bad: O(n²)
result = ""
for item in items:
    result += str(item)

# ✅ Good: O(n)
result = "".join(str(item) for item in items)

# ❌ Bad: Multiple passes
text = text.replace('a', 'x')
text = text.replace('b', 'y')

# ✅ Good: Single pass
table = str.maketrans({'a': 'x', 'b': 'y'})
text = text.translate(table)
```

## Memory Optimization

```python
# ❌ Bad: Creates intermediate lists
filtered = [x for x in data if x > 0]
doubled = [x * 2 for x in filtered]
sorted_data = sorted(doubled)

# ✅ Good: Single comprehension
result = sorted([x * 2 for x in data if x > 0])

# ❌ Bad: Loads entire file
with open(file) as f:
    lines = f.readlines()

# ✅ Good: Stream processing
with open(file) as f:
    for line in f:  # Lazy iteration
        process(line)
```

## Caching Patterns

```python
from functools import lru_cache

# ❌ Bad: No caching
def expensive_function(x):
    return complex_calculation(x)

# ✅ Good: Memoization
@lru_cache(maxsize=128)
def expensive_function(x):
    return complex_calculation(x)
```

## Database Optimization

```python
# ❌ Bad: N+1 queries
users = User.objects.all()
for user in users:
    user.posts = Post.objects.filter(user=user)

# ✅ Good: Single query with join
users = User.objects.prefetch_related('posts').all()

# ❌ Bad: No indexes
# Query: SELECT * FROM users WHERE email = '...'

# ✅ Good: Add index
# CREATE INDEX idx_user_email ON users(email);
```

## Async Operations

```python
# ❌ Bad: Sequential requests
import requests
results = []
for url in urls:
    results.append(requests.get(url).json())

# ✅ Good: Concurrent requests
import asyncio
import aiohttp

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        return await asyncio.gather(*tasks)
```

## List vs Generator

```python
# ❌ Bad: Creates full list in memory
def process_large_data():
    return [expensive_op(x) for x in range(1000000)]

# ✅ Good: Generator (lazy evaluation)
def process_large_data():
    return (expensive_op(x) for x in range(1000000))
```

## Common Anti-Patterns

### 1. Global State
```python
# ❌ Bad
counter = 0
def increment():
    global counter
    counter += 1

# ✅ Good
def create_counter():
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment
```

### 2. Premature Optimization
```python
# ❌ Bad: Optimizing before profiling
def process(data):
    # 100 lines of complex optimized code
    # that saves 0.001 seconds

# ✅ Good: Profile first, optimize bottlenecks
def process(data):
    # Simple, readable code
    # Optimize only if profiling shows it's slow
```

### 3. Missing Error Handling
```python
# ❌ Bad: No error handling
def divide(a, b):
    return a / b  # Crashes on b=0

# ✅ Good: Handle errors
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

## Profiling Commands

```python
# CPU profiling
python -m cProfile -s cumulative script.py

# Memory profiling
python -m memory_profiler script.py

# Line profiler
kernprof -l -v script.py

# Timing specific code
import timeit
timeit.timeit('func()', setup='from __main__ import func', number=1000)
```

## Performance Testing Checklist

- [ ] Profile code to identify bottlenecks
- [ ] Check algorithm complexity (Big O)
- [ ] Use appropriate data structures
- [ ] Eliminate redundant operations
- [ ] Implement caching where appropriate
- [ ] Use built-in functions over custom loops
- [ ] Consider async for I/O-bound operations
- [ ] Add database indexes for common queries
- [ ] Test with realistic data sizes
- [ ] Benchmark before and after optimizations

## When to Optimize

1. **Always optimize:**
   - Security vulnerabilities
   - Critical path operations
   - User-facing features

2. **Consider optimizing:**
   - Operations in loops
   - Database queries
   - API calls
   - File I/O

3. **Don't optimize:**
   - One-time operations
   - Initialization code
   - Code that's already fast enough

## Rule of Thumb

> "Premature optimization is the root of all evil" - Donald Knuth

1. Make it work
2. Make it right
3. Make it fast (only if needed)
