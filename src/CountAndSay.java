public class CountAndSay {
    public String countAndSay(int n) {
        if (n==0)
            return "";
        else if (n==1)
            return "1";
        else if(n==2)
            return "11";
        String str="11";
        for (int i = 3; i <= n; i++) {
            int count=0;
            String newStr="";
            for (int j = 0; j < str.length(); j++) {
                if (j==str.length()-1){
                    if (str.charAt(j)==str.charAt(j-1)){
                        count++;
                    }else {
                        newStr+=(String.valueOf(count)+str.charAt(j-1));
                        count=1;
                    }
                    newStr+=(String.valueOf(count)+str.charAt(j));
                    break;
                }
                if (j==0) {
                    count++;
                    continue;
                }
                if (str.charAt(j)==str.charAt(j-1)){
                    count++;
                }else {
                    newStr+=(String.valueOf(count)+str.charAt(j-1));
                    count=1;
                }

            }
            str=newStr;
        }
        return str;
    }
}
