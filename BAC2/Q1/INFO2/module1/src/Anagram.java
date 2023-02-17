import java.util.Arrays;

public class Anagram {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(countAlphabet("Hello, world!")));
        System.out.println(Anagram.isAnagram("Madam Curie", "Radium came"));


    }


    /**
     * Count the number of occurrences of each letter of the alphabet
     * (from 'A' to 'Z') in the given string. The function must return
     * an array containing 26 elements: The item with index 0 contains
     * the number of 'A' in the string, the item with index 1 contains
     * the number of 'B', and so on.
     *
     * This function must be case-insensitive, i.e. the character 'f'
     * must be considered as the same as character 'F'.
     *
     * Characters that are neither in the range 'a' to 'z', nor in the
     * range 'A' to 'Z' must be ignored.
     *
     * @param s The string of interest.
     * @return An array counting the number of occurrences of each
     * letter.
     **/



    public static int[] countAlphabet(String s) {
        String alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String s1 = s.toUpperCase();
        int [] tab = new int [26];
        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < alphabetUpper.length(); j++) {
                if (s1.charAt(i)==alphabetUpper.charAt(j)){
                    tab[j]+=1;
                    break;
                }
            }
        }return tab;
    }



    /**
     * Check whether one string is an anagram of another string. It is
     * strongly advised to use the function "countAlphabet()" as a
     * building block for function "isAnagram()".
     * @param s1 The first string.
     * @param s2 The second string.
     * @return <code>true</code> iff. the two strings are anagrams.
     **/
    public static boolean isAnagram(String s1, String s2) {
        int [] a = countAlphabet(s1);
        int [] b = countAlphabet(s2);
        for (int i = 0; i < a.length; i++) {
            if(a[i]!=b[i]){
                return false;
            }
        }return true;
    }
}
