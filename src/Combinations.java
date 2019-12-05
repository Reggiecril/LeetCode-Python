import java.util.ArrayList;
import java.util.List;

public class Combinations {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> outList=new ArrayList<>();
        com(outList,new ArrayList<>(),n,k,1);
        return outList;
    }
    public void com(List<List<Integer>> outList,List<Integer> inList,int n,int k,int interval){
        if (inList.size()==k){
            outList.add(new ArrayList<>(inList));
            return;
        }
        for (int i = interval; i <=n-(k-inList.size()-1); i++) {
//            if (interval==num.length-1&&inList.size()==0&&num.length!=1)
//                break;
            inList.add(i);
            com(outList,inList,n,k,i+1);
            inList.remove(inList.size()-1);
        }
    }
}
