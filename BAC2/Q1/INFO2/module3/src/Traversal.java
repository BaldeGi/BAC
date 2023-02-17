import com.sun.source.tree.NewArrayTree;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack; // this should give you a hint for the iterative version


//Cette classe est liée à la classe Noeud pour faire les deux methode en dessous

public class Traversal {

    public static void main(String[] args) {
        ArrayList<Integer> res  = new ArrayList<>();
        ArrayList<Integer> rec = new ArrayList<>();

        Node node = new Node(10);
        node.left = new Node(1);
        node.right = new Node(2);
        node.left.left = new Node(3);
        node.left.right = new Node(4);
        node.right.left = new Node(5);

        recursiveInorder(node,res);
        iterativeInorder(node,res);
    }

    public static void recursiveInorder(Node root, List<Integer> res) {
        // YOUR CODE HERE

        if (root.left!=null) {
            recursiveInorder(root.left,res);
        }
        res.add(root.val);
        if (root.right!=null){
            recursiveInorder(root.right, res);
        }
        System.out.println(res);
    }



    public static void iterativeInorder(Node root, List<Integer> res){
        // YOUR CODE HERE
        Stack<Node> stack = new Stack<>();
        Node current =root;
        while (!stack.isEmpty()|| current!=null){
            if(current !=null){
                stack.push(current);
                current=current.left;
            }
            else{
                current = stack.pop();
                res.add(current.val);
                current = current.right;
            }

        }


    }


}