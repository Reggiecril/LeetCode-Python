import java.util.ArrayList;
import java.util.List;

public class BestTimetoBuyandSellStock {
    public int maxProfit(int[] prices) {
        int minprice=Integer.MAX_VALUE;
        int max=0;
        for (int i = 0; i < prices.length; i++) {
            if (minprice>prices[i])
                minprice=prices[i];
            if (prices[i]-minprice>max)
                max=prices[i]-minprice;

        }
        return max;
    }
}
