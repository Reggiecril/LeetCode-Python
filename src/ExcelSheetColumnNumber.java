public class ExcelSheetColumnNumber {
    public int titleToNumber(String s) {
        if (s==null||s.length()==0)
            return 0;
        int length=1;
        int total=0;
        for (int i = s.length()-1; i >=0 ; i--,length*=26) {
            if (length==1)
                total+=s.charAt(i)-'A'+1;
            else {
                total+=(s.charAt(i)-'A'+1)*length;
            }
        }
        return total;
    }
}
