import java.util.HashMap;
import java.util.Map;

public class RomanToInt {
    public int romanToInt(String s) {
        if(s=="" || s.length()==0)return 0;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        int sum=0;
        int pre=0;
        for(int i=s.length()-1;i>=0;i--){
            int cur=map.get(s.charAt(i));
            sum+=(pre>cur)?-cur:cur;
            pre=cur;
        }
        return sum;
    }
}
