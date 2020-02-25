public class SortColor {
    public void sortColors(int[] nums) {
        int low=0,high=nums.length-1;
        int count=0;
        while(count<=high){
            if (nums[count]==0){
                int temp=nums[count];
                nums[count]=nums[low];
                nums[low]=temp;
                low++;count++;
            }else if(nums[count]==1){
                count++;
            }else{
                int temp=nums[count];
                nums[count]=nums[high];
                nums[high]=temp;
                high--;
            }
        }
    }
}
