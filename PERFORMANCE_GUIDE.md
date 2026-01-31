# Performance Optimization Guide

## Overview
This guide identifies common performance issues in code and provides optimized solutions.

## Table of Contents
1. [Algorithm Complexity Issues](#algorithm-complexity-issues)
2. [Memory Management](#memory-management)
3. [String Operations](#string-operations)
4. [Database Operations](#database-operations)
5. [I/O Operations](#io-operations)
6. [Caching Strategies](#caching-strategies)
7. [Profiling and Benchmarking](#profiling-and-benchmarking)

---

## Algorithm Complexity Issues

### Issue 1: Nested Loop with O(n²) Complexity

**Inefficient Code:**
```python
# O(n²) - checking if elements from list1 exist in list2
def find_common_elements(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common.append(item1)
                break
    return common
```

**Optimized Solution:**
```python
# O(n) - using set intersection
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))
```

**Improvement:** Reduces time complexity from O(n²) to O(n).

---

### Issue 2: Repeated List Searches

**Inefficient Code:**
```python
# O(n) for each lookup
def check_membership(items, search_values):
    results = []
    for value in search_values:
        if value in items:  # O(n) for list
            results.append(value)
    return results
```

**Optimized Solution:**
```python
# O(1) for each lookup
def check_membership(items, search_values):
    items_set = set(items)  # O(n) once
    return [value for value in search_values if value in items_set]  # O(1) per lookup
```

**Improvement:** Reduces lookup time from O(n) to O(1) per search.

---

## Memory Management

### Issue 3: Creating Unnecessary Copies

**Inefficient Code:**
```python
def process_large_data(data):
    # Creates multiple copies of large data
    filtered = []
    for item in data:
        if item > 10:
            filtered.append(item)
    
    doubled = []
    for item in filtered:
        doubled.append(item * 2)
    
    return doubled
```

**Optimized Solution:**
```python
def process_large_data(data):
    # Uses generator expressions - no intermediate lists
    return [item * 2 for item in data if item > 10]
```

**Improvement:** Reduces memory usage by avoiding intermediate lists.

---

### Issue 4: Loading Entire File into Memory

**Inefficient Code:**
```python
def count_lines_with_keyword(filename, keyword):
    # Loads entire file into memory
    with open(filename, 'r') as f:
        content = f.read()
    return content.count(keyword)
```

**Optimized Solution:**
```python
def count_lines_with_keyword(filename, keyword):
    # Processes file line by line
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            if keyword in line:
                count += 1
    return count
```

**Improvement:** Processes large files without loading everything into memory.

---

## String Operations

### Issue 5: String Concatenation in Loops

**Inefficient Code:**
```python
def build_string(items):
    result = ""
    for item in items:
        result += str(item) + ","  # Creates new string each iteration
    return result[:-1]  # Remove trailing comma
```

**Optimized Solution:**
```python
def build_string(items):
    return ",".join(str(item) for item in items)
```

**Improvement:** Uses efficient string joining instead of repeated concatenation.

---

### Issue 6: Repeated String Replacements

**Inefficient Code:**
```python
def sanitize_text(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = text.replace("'", '&#x27;')
    return text
```

**Optimized Solution:**
```python
def sanitize_text(text):
    replacements = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Or even better with str.translate():
def sanitize_text_fast(text):
    translation_table = str.maketrans({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;'
    })
    return text.translate(translation_table)
```

**Improvement:** More maintainable and potentially faster with translate().

---

## Database Operations

### Issue 7: N+1 Query Problem

**Inefficient Code:**
```python
# Pseudo-code for database operations
def get_users_with_posts():
    users = db.query("SELECT * FROM users")
    for user in users:
        # N additional queries!
        user.posts = db.query(f"SELECT * FROM posts WHERE user_id = {user.id}")
    return users
```

**Optimized Solution:**
```python
def get_users_with_posts():
    # Single query with JOIN
    result = db.query("""
        SELECT u.*, p.*
        FROM users u
        LEFT JOIN posts p ON u.id = p.user_id
    """)
    # Group results by user
    return group_by_user(result)

# Or use ORM with eager loading:
def get_users_with_posts_orm():
    return User.objects.prefetch_related('posts').all()
```

**Improvement:** Reduces N+1 queries to a single query.

---

### Issue 8: Missing Database Indexes

**Problem:** Queries on non-indexed columns are slow.

**Solution:**
```sql
-- Add indexes on frequently queried columns
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_post_created ON posts(created_at);
CREATE INDEX idx_post_user ON posts(user_id);

-- Composite index for common query patterns
CREATE INDEX idx_post_user_date ON posts(user_id, created_at);
```

**Improvement:** Can reduce query time from seconds to milliseconds.

---

## I/O Operations

### Issue 9: Synchronous API Calls

**Inefficient Code:**
```python
import requests

def fetch_user_data(user_ids):
    results = []
    for user_id in user_ids:
        response = requests.get(f'https://api.example.com/users/{user_id}')
        results.append(response.json())
    return results
```

**Optimized Solution:**
```python
import asyncio
import aiohttp

async def fetch_user(session, user_id):
    async with session.get(f'https://api.example.com/users/{user_id}') as response:
        return await response.json()

async def fetch_user_data(user_ids):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_user(session, user_id) for user_id in user_ids]
        return await asyncio.gather(*tasks)

# Usage:
# results = asyncio.run(fetch_user_data(user_ids))
```

**Improvement:** Parallel requests can be 10-100x faster than sequential.

---

### Issue 10: Unbuffered File Writing

**Inefficient Code:**
```python
def write_log_entries(filename, entries):
    with open(filename, 'a') as f:
        for entry in entries:
            f.write(entry + '\n')
            f.flush()  # Force write to disk each time
```

**Optimized Solution:**
```python
def write_log_entries(filename, entries):
    with open(filename, 'a', buffering=8192) as f:
        f.writelines(entry + '\n' for entry in entries)
    # Automatic flush on close
```

**Improvement:** Reduces disk I/O operations significantly.

---

## Caching Strategies

### Issue 11: Repeated Expensive Calculations

**Inefficient Code:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Exponential time complexity
```

**Optimized Solution:**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Or iterative approach:
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

**Improvement:** Reduces time complexity from O(2^n) to O(n) or O(n) with O(n) space.

---

### Issue 12: No Response Caching

**Inefficient Code:**
```python
def get_user_profile(user_id):
    # Fetches from database every time
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")
```

**Optimized Solution:**
```python
from functools import lru_cache
import time

class UserProfileCache:
    def __init__(self, ttl=300):  # 5 minute TTL
        self.cache = {}
        self.ttl = ttl
    
    def get(self, user_id):
        if user_id in self.cache:
            data, timestamp = self.cache[user_id]
            if time.time() - timestamp < self.ttl:
                return data
        
        # Cache miss or expired
        data = db.query(f"SELECT * FROM users WHERE id = {user_id}")
        self.cache[user_id] = (data, time.time())
        return data

cache = UserProfileCache()

def get_user_profile(user_id):
    return cache.get(user_id)
```

**Improvement:** Reduces database load and improves response time.

---

## Profiling and Benchmarking

### Python Profiling Tools

```python
import cProfile
import pstats

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Your code here
    result = expensive_function()
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # Top 10 functions
    
    return result
```

### Memory Profiling

```python
from memory_profiler import profile

@profile
def memory_intensive_function():
    large_list = [i for i in range(1000000)]
    return sum(large_list)
```

### Timing Comparisons

```python
import timeit

# Compare two implementations
inefficient_time = timeit.timeit(
    'find_common_elements(list1, list2)',
    setup='from __main__ import find_common_elements, list1, list2',
    number=1000
)

efficient_time = timeit.timeit(
    'find_common_elements_optimized(list1, list2)',
    setup='from __main__ import find_common_elements_optimized, list1, list2',
    number=1000
)

print(f"Speedup: {inefficient_time / efficient_time:.2f}x")
```

---

## Best Practices

### 1. Measure Before Optimizing
- Use profiling tools to identify actual bottlenecks
- Don't optimize prematurely
- Focus on the 20% of code that takes 80% of the time

### 2. Choose the Right Data Structure
- Lists: Fast append, slow search
- Sets: Fast membership testing
- Dictionaries: Fast key-based lookup
- Deques: Fast operations at both ends

### 3. Avoid Common Pitfalls
- Don't use mutable default arguments
- Avoid global variables when possible
- Use list comprehensions over loops when appropriate
- Leverage built-in functions (they're optimized in C)

### 4. Consider Trade-offs
- Time vs. Space complexity
- Code readability vs. Performance
- Development time vs. Optimization gains

### 5. Use Appropriate Tools
- **Python:** Use PyPy for CPU-bound tasks, NumPy for numerical operations
- **JavaScript:** Use Web Workers for parallel processing
- **Java:** Use appropriate collection types, consider parallel streams
- **Databases:** Use connection pooling, prepare statements, add indexes

---

## Conclusion

Performance optimization is an iterative process:
1. **Measure** - Profile to find bottlenecks
2. **Analyze** - Understand why code is slow
3. **Optimize** - Apply appropriate optimizations
4. **Verify** - Measure improvements
5. **Iterate** - Repeat for remaining bottlenecks

Remember: "Premature optimization is the root of all evil" - Donald Knuth. Always profile first!
