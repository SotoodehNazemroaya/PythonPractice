def compute_lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp

def get_lcs(dp, str1, str2):
    i, j = len(str1), len(str2)
    lcs = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

# Example usage
str1 = "AGGTAB"
str2 = "GXTXAYB"
dp = compute_lcs(str1, str2)
lcs = get_lcs(dp, str1, str2)

print("LCS Length:", dp[len(str1)][len(str2)])
print("LCS:", lcs)
