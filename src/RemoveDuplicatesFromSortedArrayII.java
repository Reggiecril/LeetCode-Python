public class RemoveDuplicatesFromSortedArrayII {
    public static int removeDuplicates(int[] nums) {
        if (nums==null||nums.length==0)
            return 0;
        int pre=1;
        int nowInt=nums[0];
        int time=1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i]==nowInt)
            {

                if (time==2)
                    continue;
                time++;
            }else {
                nowInt=nums[i];
                time=1;

            }
            if (pre!=i){
                nums[pre]=nums[i];
            }
            pre++;
        }
        return pre;
    }
}
