import java.util.HashMap;
import java.util.Map;

public class ConstructBinaryTreefromPreorderandInorderTraversal {
    int preindex=0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder==null||inorder==null||preorder.length!=inorder.length)
            return null;
        HashMap<Integer,Integer> map=new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            map.put(inorder[i],i);
        }

        return buildTree(preorder,inorder,0,inorder.length-1,map);
    }
    public TreeNode buildTree(int[] preorder, int[] inorder, int start, int end, Map<Integer,Integer> map){
        if (start>end)
            return null;
        int index=map.get(preorder[preindex]);
        TreeNode root=new TreeNode(preorder[preindex]);
        preindex++;
        root.left=buildTree(preorder,inorder,start,index-1,map);
        root.right=buildTree(preorder,inorder,index+1,end,map);
        return root;
    }
}
