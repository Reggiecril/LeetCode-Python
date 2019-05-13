public class IntToRoman {
    public String intToRoman(int num) {
        // 100%
        int[] values={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] strs={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<values.length;i++){
            while(num>=values[i]){
                num-=values[i];
                sb.append(strs[i]);
            }
        }
        return sb.toString();

        // #82%
        // //0000,1000,2000,3000
        // String M[] = {"", "M", "MM", "MMM"};
        // //000,100,200,300,400,500,600,700,800,900
        // String C[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        // //00,10,20,30,40,50,60,70,80,90
        // String X[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        // //0,1,2,3,4,5,6,7,8,9
        // String I[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        // return M[num/1000]+C[(num%1000)/100]+X[(num%100)/10]+I[num%10];
    }
}
