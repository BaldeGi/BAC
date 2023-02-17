public class Search {
    public static void main(String[] args) {
        int [] tab = new int[]{0,1,2,3,5};
        int elem = 2;
        System.out.println(search(tab,elem));


    }

    /**
     * @param tab is an ordered array of int.
     * @return index of elem or -1
     */
    public static int search(int[] tab, int elem) {
        int low = 0;
        int high = tab.length-1;
        while (low <= high){
            int middle = (low+high)/2;
            if (tab[middle] == elem){
                return middle;
            }
            else if(elem<tab[middle]){
                high = middle-1;
            }
            else{
                low = middle+1;
            }
        }
        return -1;
    }
}
