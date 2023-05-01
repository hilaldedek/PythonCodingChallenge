# This is an interview question asked by Facebook.

#    - Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

#    - For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

#    - You can assume that the messages are decodable. For example, '001' is not allowed.

def num_decodings(s):
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]

        if i > 1 and s[i-2:i] >= '10' and s[i-2:i] <= '26':
            dp[i] += dp[i-2]
            print(dp)
    return dp[n]


print(num_decodings('121516'))
