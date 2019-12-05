import java.util.ArrayList;
import java.util.List;

public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> outList=new ArrayList<>();
        outList.add(new ArrayList<>());
        com(outList,new ArrayList<>(),nums,0);
        return outList;
    }
    public void com(List<List<Integer>> outList,List<Integer> inList,int[] nums,int interval){

        if (interval==nums.length)
            return;
        for (int i = interval; i < nums.length; i++) {
            inList.add(nums[i]);
            outList.add(new ArrayList<>(inList));
            com(outList,inList,nums,i+1);
            inList.remove(inList.size()-1);
        }
    }
}
