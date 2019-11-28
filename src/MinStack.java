import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class MinStack {
    List<Integer> list;
    Stack<Integer> stack;
    /** initialize your data structure here. */
    public MinStack() {
        list=new ArrayList<>();
        stack=new Stack<>();
    }

    public void push(int x) {
        stack.push(x);
        if (list.isEmpty())
            list.add(x);
        else {
            for (int i = 0; i < list.size(); i++) {
                if (x < list.get(i)) {
                    list.add(i, x);
                    break;
                }
            }
        }
    }

    public void pop() {
        Integer x=stack.pop();
        list.remove(x);
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return list.get(0);
    }

}