public class TreeSame {

    /* Cette classe utilise aussi la classe Node*/

    public static void main(String[] args) {
        Node root = new Node(3);
        Tree tree = new Tree(root);

        Node root2 = new Node(5);
        root2.left = new Node(4);
        root2.right = new Node(3);
        root2.left.left = new Node(0);
        root2.left.right = new Node(-1);
        Tree tree2 = new Tree(root2);

        Node root3 = new Node(3);
        Tree tree3 = new Tree(root3);

        System.out.println(tree.equals(tree2));

    }



    public static class Tree {

        public Node root;

        public Tree(Node root){
            this.root = root;
        }

        @Override
        public boolean equals(Object o) {
            if (o==null) return false;
            if(o.getClass()!=this.getClass()) return false;
            Tree t = (Tree) o;
            if (t.root==null&& this.root==null)return true;
            else if (t.root==null || this.root==null) {
                return false;
            }
            else if(this.root.val==t.root.val){

                return this.root.left.equals(t.root.left) && this.root.right.equals(t.root.right);
            }
            return false;
        }

    }

    public static class Node {

        public int val;
        public Node left;
        public Node right;

        public Node(int val){
            this.val = val;
        }

        public boolean isLeaf(){
            return this.left == null && this.right == null;
        }

        @Override
        public boolean equals(Object o){
            // YOUR CODE HERE
            Node a = (Node) o;
            if (this.right.isLeaf() == a.right.isLeaf()){
                if (this.left.isLeaf() == a.left.isLeaf()){
                    return this.right.val == a.right.val && this.left.val == a.left.val;
                }
                return false;
            }
            return false;
        }
    }



}
