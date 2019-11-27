import java.util.ArrayList;
import java.util.List;

public class BinaryTreeZigzagLevelOrderTraversal {
    // public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    //     List<List<Integer>> outList=new ArrayList<>();
    //     if(root==null)
    //         return outList;
    //     Queue<TreeNode> queue=new LinkedList<>();
    //     queue.add(root);
    //     Stack<TreeNode> stack=new Stack<>();
    //     int count=0;
    //     while (!queue.isEmpty()||!stack.empty()){
    //         if (!queue.isEmpty()){
    //             stack.push(queue.poll());
    //         }else if (queue.isEmpty()&&!stack.empty()){
    //             List<Integer> inList=new ArrayList<>();
    //             while (!stack.empty()){
    //                 TreeNode node=stack.pop();
    //                 if (count%2==0) {
    //                     if (node.left != null)
    //                         queue.add(node.left);
    //                     if (node.right != null)
    //                         queue.add(node.right);
    //                 }else {
    //                     if (node.right != null)
    //                         queue.add(node.right);
    //                     if (node.left != null)
    //                         queue.add(node.left);
    //                 }
    //                 inList.add(node.val);
    //             }
    //             outList.add(inList);
    //             count++;
    //         }
    //     }
    //     return outList;
    // }
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
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
        if (count%2==0)
            outList.get(count++).add(root.val);
        else
            outList.get(count++).add(0,root.val);

        getOrder(root.left,outList,count);
        getOrder(root.right,outList,count);
    }
}
