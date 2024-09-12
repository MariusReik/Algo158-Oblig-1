def boyer_moore(pattern, text):
    """
    Performs Boyer-Moore pattern matching and counts the number of comparisons.   
    Returns:
    - tuple: (index where pattern was found, number of comparisons)
    """
    m, n = len(pattern), len(text)
    comparisons = 0
    
    # Initialize the bad character table
    bad_character_table = {pattern[i]: i for i in range(m)}
    
    # Start with the end of the pattern and text
    i = m - 1
    j = m - 1
    
    while i < n:
        comparisons += 1
        
        if text[i] == pattern[j]:
            if j == 0:
                return i, comparisons  # Pattern found
            else:
                i -= 1
                j -= 1
        else:
            
            shift = max(1, j - bad_character_table.get(text[i], -1))
            i += shift
            j = m - 1
    
    return -1, comparisons  # Pattern not found

# Example Lorem Ipsum
text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
pattern = "ullamco"

result_index, total_comparisons = boyer_moore(pattern, text)
print(f"Pattern found at index {result_index}, comparisons: {total_comparisons}, average comparisons per character: {total_comparisons / len(text):.2f}")
