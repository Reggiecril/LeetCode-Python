import java.util.*;

public class PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> outList=new ArrayList<>();
        for(int i=0;i<numRows;i++){
            if(i==0)
                outList.add(Arrays.asList(1));
            else if (i==1)
                outList.add(Arrays.asList(1,1));
            else {
                List<Integer> inList=new ArrayList<>();
                inList.add(1);
                for(int j=1;j<i;j++){
                    inList.add(outList.get(i-1).get(j-1)+outList.get(i-1).get(j));
                }
                inList.add(1);
                outList.add(inList);
            }

        }
        return outList;
    }
}
