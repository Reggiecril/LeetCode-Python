
public class MergeSortedArray{
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        m--;
        n--;
        int length=nums1.length-1;
        while (m>=0&&n>=0){
            nums1[length--]=nums1[m]>=nums2[n]?nums1[m--]:nums2[n--];
        }
        System.arraycopy(nums2, 0, nums1, 0, n + 1);

    }
}