public class ExcelSheetColumnTitle {
    public String convertToTitle(int n) {
        StringBuilder str=new StringBuilder();
        while (n>0){
            if (n>26)
                if (n%26==0){
                    str.append('Z');
                }else {
                    str.append((char) ('A' + n % 26 - 1));
                }
            else {
                str.append((char)('A'+n-1));
                break;
            }
            if (n%26==0)
                n=(n-26)/26;
            else
                n=(n-n%26)/26;
        }
        return str.reverse().toString();
    }
}
