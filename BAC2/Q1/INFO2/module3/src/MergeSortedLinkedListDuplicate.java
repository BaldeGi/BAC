import java.util.LinkedList;

/**
 * Question:
 *
 * You are asked to merge two sorted linked lists (see the TODO below) but you need to
 * keep only one node for each distinct value
 *
 * Once it is done, copy-paste the complete class in Inginious, including the imports
 *
 *
 * Feel free to add methods or fields in the class, but do not modify
 * the signature and behavior of existing code
 *
 */
public class MergeSortedLinkedListDuplicate {

    public static void main(String[] args) {
        MergeSortedLinkedListDuplicate.Node list1 = null;
        list1 = new MergeSortedLinkedListDuplicate.Node(7, list1);
        list1 = new MergeSortedLinkedListDuplicate.Node(3, list1);
        list1 = new MergeSortedLinkedListDuplicate.Node(1, list1);
        list1 = new MergeSortedLinkedListDuplicate.Node(1, list1);

        MergeSortedLinkedListDuplicate.Node list2 = null;
        list2 = new MergeSortedLinkedListDuplicate.Node(7, list2);
        list2 = new MergeSortedLinkedListDuplicate.Node(7, list2);
        list2 = new MergeSortedLinkedListDuplicate.Node(4, list2);
        list2 = new MergeSortedLinkedListDuplicate.Node(2, list2);
        list2 = new MergeSortedLinkedListDuplicate.Node(2, list2);

        System.out.println(merge(list1,list2));

    }


    /**
     * You receive two linked lists containing elements in increasing order.
     * You are asked to return a new linked list that contains the
     * elements of both linked lists in increasing order but without duplicates.
     * The input linked lists must remain unchanged.
     * Moreover, the final linkedList must not contain duplicate values
     * That is, instead of 1-1-2-5, you must return 1-2-5.
     *
     * The complexity of your method must be in O(n+m)
     * where n = size of list1, m = size of list2
     * @param list1 the first list containing elements in increasing order
     * @param list2 the second list containing elements in increasing order
     * @return a list that contains the elements of list1 and list2 in increasing order without duplicates
     */
    public static LinkedList<Node> merge(Node list1, Node list2) {
        // TODO
        LinkedList<Node> liste = new LinkedList<>();
        LinkedList<Node> liste2 = new LinkedList<>();
        Node current = list1;
        while(current!=null){
            liste.add(current);
            current=current.next;
        }
        Node current1 = list2;
        while(current1!=null){
            liste.add(current1);
            current1=current1.next;
        }
        for (int i = 0; i < liste.size(); i++) {
            int count= 1;
            for (int j = i; j < liste.size(); j++) {
                if(liste.get(i)==liste.get(j)){
                    count++;
                }
            }
            if(count==1) {
                liste2.add(liste.get(i));
            }
        }return liste2;
    }


    static class Node {

        int value;
        Node next;

        public Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }

    }
}