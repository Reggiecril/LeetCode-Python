import java.util.ArrayList;
import java.util.List;

public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root==null)
            return new ArrayList<List<Integer>>();
        List<List<Integer>> outList=new ArrayList<>();
        getOrder(root,outList,0);
        return outList;
    }
    private void getOrder(TreeNode root, List<List<Integer>> outList,int count){
        if (root==null)
            return;
        if (outList.size()<=count)
            outList.add(new ArrayList<>());
        outList.get(count++).add(root.val);
        getOrder(root.left,outList,count);
        getOrder(root.right,outList,count);
    }
}
