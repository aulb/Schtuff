import java.lang.*;

public class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int maxInt = prices[0]; 
        int minInt = prices[0];
        int greatestDiff = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] > maxInt) {
                maxInt = prices[i];
                if (maxInt - minInt > greatestDiff) {
                    greatestDiff = maxInt - minInt;
                }
            } else if (minInt > prices[i]) {
                // Reset max if found
                maxInt = prices[i];
                // Only keep min if its smaller
                minInt = Math.min(minInt, prices[i]);
            }
        }
        return greatestDiff;
    }
}