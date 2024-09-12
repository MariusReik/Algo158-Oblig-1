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

def measure_time():
    for n in range(1, 15):  # Increased range for more noticeable results
        str1 = "a" * n
        str2 = "b" * n

        # Measure time for recursive version
        start_rec = time.perf_counter()
        lcs_recursive(str1, str2, len(str1), len(str2))
        end_rec = time.perf_counter()
        print(f"Recursive n={n}: {end_rec - start_rec:.6f} seconds")

        # Measure time for dynamic programming version
        start_dp = time.perf_counter()
        lcs_length(str1, str2)
        end_dp = time.perf_counter()
        print(f"Dynamic Programming n={n}: {end_dp - start_dp:.6f} seconds")

if __name__ == "__main__":
    measure_time()
