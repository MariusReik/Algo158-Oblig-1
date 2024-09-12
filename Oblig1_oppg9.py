import time

def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m - 1, n), lcs_recursive(X, Y, m, n - 1))

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def measure_time(func, *args, repetitions=10):
    total_time = 0.0
    for _ in range(repetitions):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    average_time = total_time / repetitions
    return result, average_time

# Test different lengths
lengths = [5, 10, 20, 25, 30, 50, 100, 1000] 
for length in lengths:
    X = "a" * length
    Y = "a" * length
    
    try:
        lcs_recursive_result, recursive_time = measure_time(lcs_recursive, X, Y, len(X), len(Y))
        print(f"Recursive LCS for length {length}: {lcs_recursive_result} (Time: {recursive_time:.4f}s)")
    except RecursionError:
        print(f"Recursive failed")

    lcs_dynamic_result, dynamic_time = measure_time(lcs_length, X, Y)
    print(f"Dynamic LCS for length {length}: {lcs_dynamic_result} (Time: {dynamic_time:.4f}s)")
