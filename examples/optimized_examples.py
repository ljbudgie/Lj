"""
Optimized Code Examples
These examples demonstrate efficient implementations of common patterns.
"""

from functools import lru_cache
from collections import Counter


def set_based_search(list1, list2):
    """
    OPTIMIZED: O(n) complexity using set intersection
    Much faster for large lists
    """
    return list(set(list1) & set(list2))


def set_based_lookups(items, search_values):
    """
    OPTIMIZED: O(n+m) where n=len(items), m=len(search_values)
    Each lookup in a set is O(1)
    """
    items_set = set(items)
    return [value for value in search_values if value in items_set]


def efficient_string_join(items):
    """
    OPTIMIZED: Uses str.join() which is optimized in C
    O(n) time complexity
    """
    return ",".join(str(item) for item in items)


def stream_file_processing(filename):
    """
    OPTIMIZED: Processes file line by line
    Constant memory usage regardless of file size
    """
    try:
        with open(filename, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0


def optimized_string_operations(text):
    """
    OPTIMIZED: Single pass using str.translate()
    Much faster than multiple replace() calls
    """
    translation_table = str.maketrans({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;'
    })
    return text.translate(translation_table)


@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    OPTIMIZED: Uses memoization to cache results
    O(n) time complexity with O(n) space
    """
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)


def fibonacci_iterative(n):
    """
    OPTIMIZED: Iterative approach
    O(n) time, O(1) space complexity
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def process_with_comprehension(data):
    """
    OPTIMIZED: Single list comprehension
    Minimal memory overhead, more Pythonic
    """
    return sorted([item * 2 for item in data if item > 10])


def check_duplicates_efficient(items):
    """
    OPTIMIZED: O(n) complexity using Counter
    Single pass through the data
    """
    counts = Counter(items)
    return [item for item, count in counts.items() if count > 1]


def closure_accumulator():
    """
    OPTIMIZED: Uses closure instead of global variable
    Thread-safe and easier to test
    """
    counter = 0
    
    def increment():
        nonlocal counter
        counter += 1
        return counter
    
    return increment


def binary_search_optimized(sorted_data, target):
    """
    OPTIMIZED: Binary search on sorted data
    O(log n) complexity vs O(n) for linear search
    """
    left, right = 0, len(sorted_data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_data[mid] == target:
            return mid
        elif sorted_data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


class SearchOptimizer:
    """
    OPTIMIZED: Pre-processes data for repeated searches
    Trades space for time when doing multiple searches
    """
    
    def __init__(self, data):
        self.data = sorted(data)
        self.index_map = {value: idx for idx, value in enumerate(data)}
    
    def search(self, target):
        """O(1) lookup using hash map"""
        return self.index_map.get(target, -1)
    
    def binary_search(self, target):
        """O(log n) lookup on sorted data"""
        return binary_search_optimized(self.data, target)


def batch_process_generator(items, batch_size=100):
    """
    OPTIMIZED: Processes data in batches using generators
    Memory efficient for large datasets
    """
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        yield [item * 2 for item in batch if item > 10]


def parallel_processing_example(data):
    """
    OPTIMIZED: Uses multiprocessing for CPU-intensive tasks
    Note: Only beneficial for CPU-bound operations on large datasets
    """
    from multiprocessing import Pool
    import os
    
    def process_chunk(chunk):
        return [item * 2 for item in chunk if item > 10]
    
    # Split data into chunks
    num_processes = os.cpu_count()
    chunk_size = len(data) // num_processes
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_chunk, chunks)
    
    # Flatten results
    return [item for chunk in results for item in chunk]


if __name__ == "__main__":
    # Example usage and timing demonstrations
    import time
    
    # Test set-based search
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    start = time.time()
    result = set_based_search(list1, list2)
    end = time.time()
    print(f"Set-based search: {end - start:.6f}s, found {len(result)} common elements")
    
    # Test efficient string join
    items = list(range(10000))
    start = time.time()
    result = efficient_string_join(items)
    end = time.time()
    print(f"Efficient string join: {end - start:.6f}s")
    
    # Test cached fibonacci
    start = time.time()
    result = fibonacci_cached(30)
    end = time.time()
    print(f"Cached fibonacci(30): {end - start:.6f}s, result = {result}")
    
    # Test iterative fibonacci
    start = time.time()
    result = fibonacci_iterative(30)
    end = time.time()
    print(f"Iterative fibonacci(30): {end - start:.6f}s, result = {result}")
    
    # Compare search methods
    data = list(range(10000))
    optimizer = SearchOptimizer(data)
    
    target = 7500
    start = time.time()
    for _ in range(1000):
        result = optimizer.search(target)
    end = time.time()
    print(f"Hash-based search (1000 iterations): {end - start:.6f}s")
    
    start = time.time()
    for _ in range(1000):
        result = optimizer.binary_search(target)
    end = time.time()
    print(f"Binary search (1000 iterations): {end - start:.6f}s")
