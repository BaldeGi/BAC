import java.util.Arrays;

public class CommonElements {
    public static void main(String[] args) {
        int [] tab1 = new int[]{1,3,5,5,4,2};
        int [] tab2 = new int []{1,2,5,5,6};
        System.out.println(count(tab1,tab2));

        int [][] tab3 = new int [][]{{1,3,5,5,4,2},{1,2,5,5,6}};
        int [][] tab4 = new int [][]{{1,3,5,5,4,2},{1,2,5,5,6}};
        System.out.println(count(tab3,tab4));
    }

    /**
     *
     * @param tab1 is a non null array
     * @param tab2 is a non null array
     * @return the number of elements that are the same at the same index
     *         more exactly the size of set {i such that tab1[i] == tab2[i]}
     *         for instance count([1,3,5,5],[1,2,5,5,6]) = 3
     */
    public static int count(int [] tab1, int [] tab2) {
        int len = Integer.min(tab1.length,tab2.length);
        int count =0;
        for (int i = 0; i < len; i++) {
            if(tab1[i]==tab2[i]) count++;
        }
        return count;
    }

    /**
     *
     * @param tab1 is a non null 2D array
     * @param tab2 is a non null 2D array
     * @return the number of elements that are the same at the same index
     *         more exactly the size of set {(i,j) such that tab1[i][j] == tab2[i][j]}
     */
    public static int count(int [][] tab1, int [][] tab2) {
        int len1 = Integer.min(tab1.length,tab2.length);
        int len2 = Integer.min(tab1[0].length,tab2[0].length);
        int count =0;
        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                if(tab1[i][j]==tab2[i][j]){
                    count++;
                }
            }
        }
        return count;
    }
}
