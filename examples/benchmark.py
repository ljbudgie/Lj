"""
Performance Benchmark Script
Compares inefficient vs optimized implementations
"""

import time
import sys
from pathlib import Path

# Add parent directory to path to import examples
sys.path.insert(0, str(Path(__file__).parent))

from inefficient_examples import (
    nested_loop_search,
    repeated_list_lookups,
    string_concatenation_loop,
    multiple_string_operations,
    fibonacci_recursive,
    process_with_intermediate_lists,
    check_duplicates_naive,
    unoptimized_search
)

from optimized_examples import (
    set_based_search,
    set_based_lookups,
    efficient_string_join,
    optimized_string_operations,
    fibonacci_cached,
    fibonacci_iterative,
    process_with_comprehension,
    check_duplicates_efficient,
    binary_search_optimized
)


def benchmark(func, *args, iterations=1):
    """Run a function multiple times and return average time"""
    total_time = 0
    result = None
    
    for _ in range(iterations):
        start = time.time()
        result = func(*args)
        end = time.time()
        total_time += (end - start)
    
    return total_time / iterations, result


def format_time(seconds):
    """Format time in human-readable format"""
    if seconds < 0.001:
        return f"{seconds * 1000000:.2f} μs"
    elif seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    else:
        return f"{seconds:.4f} s"


def print_comparison(name, inefficient_time, optimized_time):
    """Print comparison with speedup factor"""
    speedup = inefficient_time / optimized_time if optimized_time > 0 else float('inf')
    print(f"\n{name}")
    print(f"  Inefficient: {format_time(inefficient_time)}")
    print(f"  Optimized:   {format_time(optimized_time)}")
    print(f"  Speedup:     {speedup:.2f}x faster")


def main():
    print("=" * 70)
    print("PERFORMANCE BENCHMARK COMPARISON")
    print("=" * 70)
    
    # Test 1: Common elements search
    print("\n" + "=" * 70)
    print("Test 1: Finding Common Elements")
    print("=" * 70)
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    inefficient_time, result1 = benchmark(nested_loop_search, list1, list2)
    optimized_time, result2 = benchmark(set_based_search, list1, list2)
    
    print(f"Lists: {len(list1)} and {len(list2)} elements")
    print(f"Common elements found: {len(result1)}")
    print_comparison("Nested loops vs Set intersection", inefficient_time, optimized_time)
    
    # Test 2: List lookups
    print("\n" + "=" * 70)
    print("Test 2: Multiple Membership Checks")
    print("=" * 70)
    items = list(range(5000))
    search_values = list(range(0, 10000, 10))
    
    inefficient_time, result1 = benchmark(repeated_list_lookups, items, search_values)
    optimized_time, result2 = benchmark(set_based_lookups, items, search_values)
    
    print(f"Items: {len(items)}, Searches: {len(search_values)}")
    print(f"Matches found: {len(result1)}")
    print_comparison("List lookups vs Set lookups", inefficient_time, optimized_time)
    
    # Test 3: String concatenation
    print("\n" + "=" * 70)
    print("Test 3: String Building")
    print("=" * 70)
    items = list(range(5000))
    
    inefficient_time, _ = benchmark(string_concatenation_loop, items)
    optimized_time, _ = benchmark(efficient_string_join, items)
    
    print(f"Items to concatenate: {len(items)}")
    print_comparison("String concatenation vs join()", inefficient_time, optimized_time)
    
    # Test 4: String replacements
    print("\n" + "=" * 70)
    print("Test 4: Multiple String Replacements")
    print("=" * 70)
    text = "Hello <world> & 'everyone' with \"quotes\"" * 100
    
    inefficient_time, _ = benchmark(multiple_string_operations, text, iterations=100)
    optimized_time, _ = benchmark(optimized_string_operations, text, iterations=100)
    
    print(f"Text length: {len(text)} characters")
    print_comparison("Multiple replace() vs translate()", inefficient_time, optimized_time)
    
    # Test 5: Fibonacci (careful with recursive version!)
    print("\n" + "=" * 70)
    print("Test 5: Fibonacci Calculation")
    print("=" * 70)
    n = 25  # Keep it reasonable for recursive version
    
    inefficient_time, result1 = benchmark(fibonacci_recursive, n)
    
    # Test with cold cache (first call)
    fibonacci_cached.cache_clear()
    cold_cache_time, result2 = benchmark(fibonacci_cached, n)
    
    # Test with warm cache (subsequent calls)
    warm_cache_time, result3 = benchmark(fibonacci_cached, n, iterations=100)
    
    iterative_time, result4 = benchmark(fibonacci_iterative, n)
    
    print(f"Calculating fibonacci({n})")
    print(f"Result: {result1}")
    print(f"\nRecursive:      {format_time(inefficient_time)}")
    print(f"Cached (cold):  {format_time(cold_cache_time)} ({inefficient_time/cold_cache_time:.2f}x faster)")
    print(f"Cached (warm):  {format_time(warm_cache_time)} ({inefficient_time/warm_cache_time:.2f}x faster)")
    print(f"Iterative:      {format_time(iterative_time)} ({inefficient_time/iterative_time:.2f}x faster)")
    
    # Test 6: Data processing
    print("\n" + "=" * 70)
    print("Test 6: Data Processing with Filtering and Transformation")
    print("=" * 70)
    data = list(range(10000))
    
    inefficient_time, result1 = benchmark(process_with_intermediate_lists, data)
    optimized_time, result2 = benchmark(process_with_comprehension, data)
    
    print(f"Input data: {len(data)} items")
    print(f"Output data: {len(result1)} items")
    print_comparison("Multiple loops vs Comprehension", inefficient_time, optimized_time)
    
    # Test 7: Finding duplicates
    print("\n" + "=" * 70)
    print("Test 7: Finding Duplicate Elements")
    print("=" * 70)
    items = [1, 2, 3, 4, 5] * 100 + [6, 7, 8] * 50
    
    inefficient_time, result1 = benchmark(check_duplicates_naive, items)
    optimized_time, result2 = benchmark(check_duplicates_efficient, items)
    
    print(f"Items: {len(items)}")
    print(f"Duplicates found: {len(result1)}")
    print_comparison("Nested loops vs Counter", inefficient_time, optimized_time)
    
    # Test 8: Search operations
    print("\n" + "=" * 70)
    print("Test 8: Search Operations (1000 searches)")
    print("=" * 70)
    data = list(range(10000))
    sorted_data = sorted(data)
    target = 7500
    
    linear_time = 0
    binary_time = 0
    
    for _ in range(1000):
        start = time.time()
        unoptimized_search(data, target)
        linear_time += time.time() - start
        
        start = time.time()
        binary_search_optimized(sorted_data, target)
        binary_time += time.time() - start
    
    print(f"Data size: {len(data)}, Target: {target}")
    print_comparison("Linear search vs Binary search", linear_time, binary_time)
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
Key Takeaways:
1. Use appropriate data structures (sets for membership testing)
2. Avoid nested loops when possible
3. Use built-in functions (join, translate) - they're optimized in C
4. Implement memoization for recursive algorithms
5. Use comprehensions for cleaner and faster code
6. Choose the right algorithm complexity for your use case
    """)


if __name__ == "__main__":
    main()
