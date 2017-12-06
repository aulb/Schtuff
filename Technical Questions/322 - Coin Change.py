class Solution:
    # Same as perfectSquares
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Need float inf cause maxsize causes overflow
        dp = [0] + [float('inf')] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
        
        return [dp[amount], -1][dp[amount] == float('inf')]
