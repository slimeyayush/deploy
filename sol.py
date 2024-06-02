def max_common_subsequence_length(S1, S2, K):
    len_s1, len_s2 = len(S1), len(S2)

    # Initialize a 2D table to store the length of the common subsequence
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    # Fill the table using dynamic programming
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if abs(ord(S1[i - 1]) - ord(S2[j - 1])) <= K:
                dp[i][j] = dp[i - 1][j - 1] + 1
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])

    return dp[len_s1][len_s2]

# Input reading
S1 = input().strip()
S2 = input().strip()
K = int(input())

# Call the function and print the result
result = max_common_subsequence_length(S1, S2, K)
print(result)