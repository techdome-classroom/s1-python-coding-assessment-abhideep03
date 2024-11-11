def decode_message( s: str, p: str) -> bool:
    m, n = len(message), len(key)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if key[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif key[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] and message[i - 1] == key[j - 1]

    return dp[m][n]