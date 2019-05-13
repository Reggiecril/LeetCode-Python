public class ReverseInteger {
    public int reverse(int x) {
        int sign = (x > 0) ? 1 : -1;
        long g = Math.abs(x);
        long re = 0;
        while (g > 0) {
            long count = g % 10;
            re = re * 10 + count;
            g /= 10;
        }
        if (re * sign > Integer.MAX_VALUE)
            return 0;
        else if (re * sign < Integer.MIN_VALUE)
            return 0;
        return (int) re * sign;
    }
}
