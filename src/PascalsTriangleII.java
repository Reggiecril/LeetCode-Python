import java.util.*;

public class PascalsTriangleII {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> pre=new ArrayList<>();
        rowIndex++;
        if (rowIndex==1) {
            pre.add(1);
            return pre;
        }else if(rowIndex==2)
        {
            pre.add(1);
            pre.add(1);
            return pre;
        }else {
            pre.add(1);
            pre.add(1);
        }
        for (int i = 3; i <= rowIndex; i++) {
            List<Integer> cur=new ArrayList<>();

            for (int j = 0; j < i; j++) {
                if (j==0)
                    cur.add(1);
                else if (j==i-1){
                    cur.add(1);
                    pre=new ArrayList<>(cur);
                }else {
                    cur.add(pre.get(j-1)+pre.get(j));
                }
            }
        }
        return pre;
    }
}
