import java.util.ArrayList;
import java.util.List;

public class Tree {
    public Noeud root;


    public static void main(String[] args) {

        Noeud Noeud = new Noeud(10);
        Noeud.left = new Noeud(1);
        Noeud.right = new Noeud(2);
        Noeud.left.left = new Noeud(3);
        Noeud.left.right = new Noeud(4);
        Noeud.right.left = new Noeud(5);

        Noeud Noeud1 = new Noeud(10);
        Noeud1.left = new Noeud(1);
        Noeud1.right = new Noeud(2);
        Noeud1.left.left = new Noeud(13);
        Noeud1.left.right = new Noeud(4);
        Noeud1.right.left = new Noeud(5);

        Tree tree = new Tree(Noeud);
        Tree tree1 = new Tree(Noeud1);

        System.out.println(tree);

    }

    public Tree(Noeud root){
        this.root = root;
    }




    public Tree combineWith(Tree o){
        // YOUR CODE HERE


    }



}




