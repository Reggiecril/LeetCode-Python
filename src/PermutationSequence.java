import java.util.ArrayList;
import java.util.List;

public class PermutationSequence {
    public String getPermutation(int n, int k) {
        if (n==0||k==0||k>foo(n))
            return "";
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            list.add(i);
        }
        return getPermutation(list,k);
    }

    public String getPermutation(List<Integer> list, int k) {
        if (list.size()==1)
            return String.valueOf(list.get(0));
        int size=list.size();
        int preSize=foo(size-1);
        int mod=k%preSize;
        if(mod==0)
            mod=preSize;
        int poistion= (int) Math.ceil((double)(k)/(double)(preSize));
        int getInt=list.remove(poistion-1);
        return getInt+getPermutation(list,mod);
    }

    public int foo(int n) {
        if (n == 1)
            return 1;
        else if (n == 2)
            return 2;
        return n * foo(n - 1);
    }
}
