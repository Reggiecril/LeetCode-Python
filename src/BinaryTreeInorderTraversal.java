import java.util.ArrayList;
import java.util.List;

public class BinaryTreeInorderTraversal {
    public void postorder(TreeNode root, List<Integer> list){
        if (root==null)
            return;
        postorder(root.left,list);
        list.add(root.val);
        postorder(root.right,list);


    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list=new ArrayList<>();
        postorder(root,list);
        return list;
    }
}
