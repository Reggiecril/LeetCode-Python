import java.util.*;

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
        int sign = (x > 0) ? 1 : -1;
        long g = Math.abs(x);
        long re = 0;
        while (g > 0) {
            long count = g % 10;
            re = re * 10 + count;
            g /= 10;
        }

        if ((re * sign) > Integer.MAX_VALUE)
            return 0;
        else if ((re * sign) < Integer.MIN_VALUE)
            return 0;
        return (int) re * sign;

    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
        if (candidates == null || candidates.length == 0)
            return list;
        Arrays.sort(candidates);
        combination(candidates, list, new ArrayList<>(), target, 0);
        return list;
    }

    private void combination(int[] candidates, List<List<Integer>> outList, List<Integer> inList, int target, int count) {
        if (target == 0) {
            outList.add(new ArrayList<>(inList));
            return;
        }
        if (target < 0) return;
        for (int i = count; i < candidates.length; i++) {
            if (i > count && candidates[i] == candidates[i - 1]) continue;
            inList.add(candidates[i]);
            combination(candidates, outList, inList, target - candidates[i], i + 1);
            inList.remove(inList.size() - 1);
        }


    }

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> outList=new ArrayList<>();
        if(strs==null||strs.length==0)
            return outList;
        Map<String,List<String>> map=new HashMap<>();
        for(String str:strs){
            char[] ch=str.toCharArray();
            Arrays.sort(ch);
            String newStr=String.valueOf(ch);
            if (map.containsKey(newStr)){
                map.get(newStr).add(str);
            }else{
                List<String> inList=new ArrayList<>();
                inList.add(str);
                map.put(newStr,inList);
            }

        }
        return new ArrayList<>(map.values());

    }

    public List<List<Integer>> threeSum(int[] nums) {
        if(nums.length<3 || nums==null)
            return new ArrayList<>();
        Set<List<Integer>> outList=new HashSet<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i>0 && nums[i]==nums[i-1])
                continue;
            int pre=nums[i];
            Map<Integer,Integer> map=new HashMap<>();
            for (int j = i+1; j < nums.length; j++) {
                int value=nums[j];
                int diff=-(pre+value);
                if (map.containsKey(diff)){
                    outList.add(Arrays.asList(pre,nums[map.get(diff)],value));

                }else{
                    map.put(value,j);
                }

            }
        }
        return new ArrayList<>(outList);
    }
    public static void main(String[] args) {

        Test test = new Test();
        int [][] i={{1,3},{2,6},{8,10},{15,18}};
        int []num={-1, 0, 1, 2, -1, -4};
        System.out.println(test.threeSum(num).toString());

















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