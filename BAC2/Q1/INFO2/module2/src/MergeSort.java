import java.util.Arrays;
import java.util.Scanner;

public class MergeSort {

    public static void main(String[] args) {
        int [] a = new int[]{-1,4,5,1,0,8,-10,-10000};
        System.out.println(Arrays.toString(sort(a)));
        int [] b = new int[]{-1,0,2,3,1,4,10,12};

        int [] c = new int[]{4, 5, 1, 3};
        int [] aux = new int [c.length];

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n==10){
            System.out.println("cool");
        }




    }
    /**
     * Pre-conditions: a[lo..mid] and a[mid+1..hi] are sorted
     * Post-conditions: a[lo..hi] is sorted
     */
    private static void merge(int[] a, int[] aux, int lo, int mid, int hi) {
        int k = 0;
        for (int i = lo; i < mid+1; i++) {
            int min = a[i];
            for (int j = mid+1+k; j < hi+1 ; j++) {
               if(a[j]<min){
                   min = a[j];
                   k++;
               }
            }aux[i] = min;

        }
    }
    /**
     * Rearranges the array in ascending order, using the natural order
     * @return
     */
    public static int [] sort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = i+1; j < a.length; j++) {
                if(a[i]>a[j]){
                    int tmp = a[i];
                    a[i] =a[j];
                    a[j] = tmp;
                }
            }
        }
        return a;
    }

    //TODO Optionnal additionnal method
}