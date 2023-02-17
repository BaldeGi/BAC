import java.util.Arrays;

public class Largest_sum {

    public static void main(String[] args) {
        int[] a = new int[]{-2, -3, -10, -5};
        System.out.println(Arrays.toString(maxSubArray(a)));

    }

    /**
     * Find the contiguous subarray with the maximal sum
     *
     * @param a a non-empty array
     * @return A triplet (sum, start, end) with sum the sum of the subarray and `start` and `end` the
     * start and end of the subarray
     * <p>
     * For example for the array [-2,1,-3,4,-1,2,1,-5,4] your method should return [6, 3, 6]
     */

    /*
    la deuxieme boucle j'ai mis j=i au lieu de j=i+1
    la somme doit commencer a Zero et il doit etre entre les deux boucle;
    Remplace ton sommeAux en max et tu l'initialise a a[0];
    la res enlève les accolades et met 3 dans les crochets comme ça tu aura ça [0,0,0] quand tu le print;
    achaque fois que somme>max ==> max=somme;
    creer des variable qui sera i et j quand somme>max et que max=somme;

    pour eviter de  mettre a.lenght-1 ou d'avoir une index out je te conseille de cree une nouvelle list
    dans une autre methode pour augmente la taille da la list a +1.
     */
    public static int[] maxSubArray(int[] a) {
        int debut=0;
        int fin =0;
        int max =a[0];
        int[] res = new int[3];
        for (int i = 0; i < a.length; i++) {
            int somme = 0;
            for (int j = i; j < a.length-1; j++) {
                somme+=a[j];
                if (somme > max) {
                    max = somme;
                    debut = i;
                    fin = j;
                }else if(somme+a[j+1]<a[j+1]){
                    i=j;
                    break;
                }
            }
        }
        res[0] = max;
        res[1] = debut;
        res[2] =fin;
        return res;
    }
}
