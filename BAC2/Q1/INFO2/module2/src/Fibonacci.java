import java.util.Arrays;
import java.util.Scanner;

public class Fibonacci {

    public static void main(String[] args) {
        System.out.println(fiboIterative(1));
        System.out.println(fiboRecursive(11));

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
    }

    /*
     * Returns the index-th element of the fibonnaci sequence, computed recursively
     */
    public static int fiboRecursive(int index){
       if(index==0){
           return 0;
       }
       else if(index==1){
           return 1;
        }
       else{
           return fiboRecursive(index-1)+fiboRecursive(index-2);
       }
    }

    /*
     * Returns the index-th element of the fibonnaci sequence, computed iteratively
     */
    public static int fiboIterative(int index){
        if(index==1){return 1;}
        else if(index==0){return 0;}
        int [] tab = new int[index+1];
        tab[1] = 1;
        int indice = 2;
        if(index==1) return 0;
        for (int i = 2; i < index; i++) {
            tab[i] = tab[i-1]+tab[i-2];
            indice++;
        }
        tab[indice] = tab[indice-1]+tab[indice-2];
        return tab[tab.length-1];
    }

}

