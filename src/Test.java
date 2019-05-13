import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Test {

    public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            list.add(node.val);
            if (node.left != null)
                queue.offer(node.left);
            if (node.right != null)
                queue.offer(node.right);

        }
        return list;
    }

    public int reverse(int x) {
        int sign=(x>0)?1:-1;
        long g=Math.abs(x);
        long re=0;
        while(g>0){
            long count=g%10;
            re=re*10+count;
            g/=10;
        }

        if ((re*sign)>Integer.MAX_VALUE)
            return 0;
        else if((re*sign)<Integer.MIN_VALUE)
            return 0;
        return (int)re*sign;

    }

    public static void main(String[] args) {

        Test test = new Test();

        //Test set--TreeNode
        TreeNode tree = new TreeNode(10);
        tree.left = new TreeNode(6);
        tree.right = new TreeNode(14);
        tree.left.left = new TreeNode(4);
        tree.left.right = new TreeNode(8);
        tree.right.left = new TreeNode(12);
        tree.right.right = new TreeNode(16);
        //ListNode
        ListNode lnode = new ListNode(10);
        lnode.next = new ListNode(6);
        lnode.next.next = new ListNode(13);
        lnode.next.next.next = new ListNode(14);
        lnode.next.next.next.next = new ListNode(15);


    }
}

class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;
    }
}

class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}