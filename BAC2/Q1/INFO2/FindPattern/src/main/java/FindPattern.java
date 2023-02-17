import java.util.Arrays;

public class FindPattern {


    public static void main(String[] args) {
        int [] a = new int[]{1, 1, 3, 5};
        int [] b = new int []{3, 1, 2, 0, 1, 3, 1, 5, 1};
        System.out.println(find(a,b));
        System.out.println(Arrays.toString(sort(a)));
    }
    /**
     * In this task you must find the first occurrence of a pattern in a
     * sequence.
     * This occurrence might also be **in a different order** than in
     * the pattern.
     *
     * For example, let:
     *      pattern = [1, 1, 3, 5]
     *      sequence = [3, 1, 2, 5, 1, 3, 1, 5, 1]
     *
     * Starting at index 3, we have the sub-sequence [5, 1, 3, 1] which
     * is the pattern reordered. Thus your method must return 3.
     * Note that the pattern also appears at index 4, but you must
     * return the first occurrence.
     * If the pattern is not in the sequence, you must return -1.
     *
     * @param pattern The pattern to look for
     * @param sequence The sequence to look in. Each element of the sequence is
     *        in the interval [0, 15]
     * @return The index of the first occurrence of the pattern in the
     *         sequence or -1 if the pattern is not in the sequence
     */
    public static int find(int [] pattern, int [] sequence) {
        int  [] list = new int [pattern.length];
        int var = pattern.length;
        for (int i = 0; i < sequence.length; i++) {
            int count =0;
            int index = i;
            boolean verfication = false;
            if(var==sequence.length+1) break;
            for (int j = i; j < var ; j++) {
                if(sequence[j]<0 || sequence[j]>15) break;
                list[count]=sequence[j];
                count++;
                if(count==pattern.length){
                    int [] l_trie = sort(list);
                    for (int k = 0; k < l_trie.length; k++) {
                        if(list[k]!=pattern[k]){
                            verfication =true;
                            break;
                        }
                    }
                    if(!verfication){
                        return index;
                    }
                    list = new int [pattern.length];
                }
            }
            var++;
        }
        return -1;
    }

    public static int [] sort(int [] a){
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
}