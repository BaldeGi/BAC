public class Noeud {

    public int val;
    public Noeud left;
    public Noeud right;


    public Noeud(int val){
        this.val = val;
    }

    public Noeud(int val, Noeud left, Noeud right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public boolean isLeaf(){
        return this.left == null && this.right == null;
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Noeud)) return false;

        Noeud other = (Noeud) o;
        if (this.isLeaf() && other.isLeaf()) {
            return this.val == other.val;
        } else if (this.isLeaf() != other.isLeaf()) {
            return false;
        } else {
            return this.val == other.val && this.left.equals(other.left) && this.right.equals(other.right);
        }
    }
}