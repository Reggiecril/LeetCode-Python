public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        if(s.trim().equals("")||s.length()==0)
            return true;
        int left=0;
        int right=s.length()-1;
        boolean bool=true;
        while (left<right){
            while (!Character.isLetterOrDigit(s.charAt(left))){
                left++;
                if (left>right)
                    break;
            }

            while (!Character.isLetterOrDigit(s.charAt(right))) {

                right--;
                if (left>right)
                    break;
            }
            if (left>right)
                break;
            char strLeft=Character.toLowerCase(s.charAt(left++));
            char strRight=Character.toLowerCase(s.charAt(right--));
            if (strLeft!=strRight){
                bool=false;
                break;
            }
        }
        return bool;
    }
}
