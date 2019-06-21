import java.util.*;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        if(nums.length<3 || nums==null)
            return new ArrayList<>();
        Set<List<Integer>> outList=new HashSet<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i>0 && nums[i]==nums[i-1])
                continue;
            int pre=nums[i];
            Map<Integer,Integer> map=new HashMap<>();
            for (int j = i+1; j < nums.length; j++) {
                int value=nums[j];
                int diff=-(pre+value);
                if (map.containsKey(diff)){
                    outList.add(Arrays.asList(pre,nums[map.get(diff)],value));

                }else{
                    map.put(value,j);
                }

            }
        }
        return new ArrayList<>(outList);
    }
}
