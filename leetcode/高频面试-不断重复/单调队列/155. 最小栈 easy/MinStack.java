/**
 * 栈的操作：isEmpty()
 *         peek()
 *         add()
 *         pop()
 */

java.util.Stack;

class MinStack {
    private Stack<Integer> stack1;  // 数据栈
    private Stack<Integer> stack2;  // 辅助栈

    /** initialize your data structure here. */
    public MinStack() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.add(x);

        if(stack2.isEmpty() || stack2.peek() >= x) {
            stack2.add(x);
        } else {
            stack2.add(stack2.peek());
        }
    }
    
    public void pop() {
        if(!stack1.isEmpty()) {
            stack1.pop();
            stack2.pop();
        }

    }
    
    public int top() {
        if(!stack1.isEmpty()) {
            return stack1.peek();
        }
        throw new RuntimeException("空栈，非法操作");
    }
    
    public int getMin() {
        if(!stack2.isEmpty()) {
            return stack2.peek();
        }
        throw new RuntimeException("空栈，非法操作");
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */