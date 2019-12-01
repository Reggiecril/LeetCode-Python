public class FindFirstandLastPositionofElementinSortedArray {
    public int[] searchRange(int[] nums, int target) {
        if(nums==null||nums.length==0)
            return new int[]{-1,-1};
        return new int[]{getResult(nums,target,true),getResult(nums,target,false)};
    }
    private int getResult(int[]nums,int target,boolean flag){
        int left=0;
        int right=nums.length-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            if (nums[mid]<target){
                left=mid+1;
            }else if (nums[mid]>target){
                right=mid-1;
            }else {
                if (flag){
                    right=mid-1;
                }else {
                    left=mid+1;
                }
            }
        }
        int res=0;
        if (flag)
            res=left<nums.length&&nums[left]==target?left:-1;
        else
            res=right>=0&&nums[right]==target?right:-1;
        return res;
    }
}
