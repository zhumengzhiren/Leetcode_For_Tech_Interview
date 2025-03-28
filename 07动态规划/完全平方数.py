def numSquares(n: int) -> int:
        i = 0
        square = []
        while i * i <= n:
            square.append(i*i)
            i += 1
        dp = [0] + [float("inf")] * n
        for j in range(1,len(square)):
            for i in range(n, -1, -1):
                if i+1 > square[j]:
                    dp[i] = min(dp[i],dp[i-square[j]]+1)
        print(dp)
        return dp[-1]




print(numSquares(13))