
def buildString(a, b, s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        # Option 1: Add next character
        dp[i + 1] = min(dp[i + 1], dp[i] + a)

        # Option 2: Find longest match starting at i
        max_len = 0
        for l in range(1, n - i + 1):
            sub = s[i:i + l]
            if sub in s[:i]:
                max_len = l
            else:
                break

        if max_len > 0:
            dp[i + max_len] = min(dp[i + max_len], dp[i] + b)

    return dp[n]
