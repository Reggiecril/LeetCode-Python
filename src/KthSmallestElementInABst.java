public class KthSmallestElementInABst {
    volatile int i=-1,ke=0;
    public synchronized int kthSmallest(TreeNode root, int k) {
        if (root==null)
            return -1;
        ke=k;
        getList(root);
        return i;
    }
    public synchronized void getList(TreeNode root){

        if (root==null)
            return;
        if (root.left!=null)
            getList(root.left);

        if (ke==1&&i==-1) {
            i=root.val;
            return;
        }else if (ke<0) {
            return;

        }
        else
            ke--;
        if (root.right!=null)
            getList(root.right);
    }
//    public synchronized int kthSmallest(TreeNode root, int k) {
//        if (root==null)
//            return -1;
//        List<Integer> list=new ArrayList<>();
//        getList(root,list,k);
//        if (!list.isEmpty())
//            return list.get(k-1);
//        return -1;
//    }
//    public synchronized void getList(TreeNode root,List<Integer> list,int k){
//        if (list.size()==k)
//            return;
//        if (root==null)
//            return;
//        if (root.left!=null)
//            getList(root.left,list,k);
//        list.add(root.val);
//        if (root.right!=null)
//            getList(root.right,list,k);
//    }
}
