"""
Examples of Inefficient Code Patterns
These examples demonstrate common performance anti-patterns.
"""


def nested_loop_search(list1, list2):
    """
    INEFFICIENT: O(n²) complexity
    Searches for common elements using nested loops
    """
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common.append(item1)
                break
    return common


def repeated_list_lookups(items, search_values):
    """
    INEFFICIENT: O(n*m) where n=len(items), m=len(search_values)
    Each lookup in a list is O(n)
    """
    results = []
    for value in search_values:
        if value in items:
            results.append(value)
    return results


def string_concatenation_loop(items):
    """
    INEFFICIENT: Creates a new string object for each concatenation
    O(n²) time complexity due to string immutability
    """
    result = ""
    for item in items:
        result += str(item) + ","
    return result[:-1] if result else ""


def load_entire_file(filename):
    """
    INEFFICIENT: Loads entire file into memory
    Problematic for large files
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return len(content.split('\n'))
    except FileNotFoundError:
        return 0


def multiple_string_operations(text):
    """
    INEFFICIENT: Multiple passes over the string
    """
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = text.replace("'", '&#x27;')
    return text


def fibonacci_recursive(n):
    """
    INEFFICIENT: Exponential time complexity O(2^n)
    Recalculates same values multiple times
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def process_with_intermediate_lists(data):
    """
    INEFFICIENT: Creates multiple intermediate lists
    High memory usage
    """
    filtered = []
    for item in data:
        if item > 10:
            filtered.append(item)
    
    doubled = []
    for item in filtered:
        doubled.append(item * 2)
    
    sorted_data = []
    for item in sorted(doubled):
        sorted_data.append(item)
    
    return sorted_data


def check_duplicates_naive(items):
    """
    INEFFICIENT: O(n²) complexity
    Compares each item with every other item
    """
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


def global_variable_accumulator():
    """
    INEFFICIENT: Uses global variable, not thread-safe
    Difficult to test and maintain
    """
    global counter
    counter = 0
    
    def increment():
        global counter
        counter += 1
        return counter
    
    return increment


def unoptimized_search(data, target):
    """
    INEFFICIENT: Linear search on unsorted data
    Could be optimized with sorting + binary search for repeated queries
    """
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


if __name__ == "__main__":
    # Example usage and timing demonstrations
    import time
    
    # Test nested loop search
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    
    start = time.time()
    result = nested_loop_search(list1, list2)
    end = time.time()
    print(f"Nested loop search: {end - start:.4f}s, found {len(result)} common elements")
    
    # Test string concatenation
    items = list(range(10000))
    start = time.time()
    result = string_concatenation_loop(items)
    end = time.time()
    print(f"String concatenation loop: {end - start:.4f}s")
    
    # Test fibonacci
    start = time.time()
    result = fibonacci_recursive(30)
    end = time.time()
    print(f"Recursive fibonacci(30): {end - start:.4f}s, result = {result}")
