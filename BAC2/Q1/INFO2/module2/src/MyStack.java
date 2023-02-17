import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;

public class MyStack<E> {

    private LinkedList<E> queue;

    public static void main(String[] args) {
        MyStack<Integer> tab = new MyStack<>();
        tab.push(1);
        tab.push(2);
        tab.push(3);
        System.out.println(tab.peek());
        System.out.println(tab.queue);
        System.out.println(tab.pop());
        System.out.println(tab.empty());
    }

    /*
     * Constructor
     */
    public MyStack() {
        this.queue = new LinkedList<>();
    }

    /**
     * Push an element on the stack
     *
     * @param elem the Element to push
     */
    public void push(E elem) {
        queue.add(0,elem);
    }

    /**
     * Remove the element at the top of the stack
     *
     * @return The element at the top of the stack
     */
    public E pop() {
        E elem = queue.remove(0);
        return elem;

        // ou return queue.remove(0)

    }

    /**
     * Look at the element at the top of the stack
     *
     * @return The element at the top of the stack
     */
    public E peek() {
       return queue.peek();
    }

    /**
     * Is the stack empty
     *
     * @return True if there is no element in the stack
     *         and false otherwise
     */
    public boolean empty() {
       return queue.isEmpty();
    }

}