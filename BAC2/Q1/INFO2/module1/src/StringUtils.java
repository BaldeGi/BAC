import java.util.Arrays;

public class StringUtils {

    public static void main(String[] args) {

        char a = '.';
        System.out.println(Arrays.toString(split("Here.I.Go",a)));
        System.out.println(indexOf("Hello", "ell"));
        System.out.println(toLowerCase("BONJOUR iCi"));
        System.out.println(palindrome("kayak"));


        /*char offset = (int) 42 ;
        System.out.println(offset);*/


    }
    /**
     * Split a string according to a delimiter
     *
     * @param str The string to split
     * @param delimiter The delimiter
     * @return An array containing the substring which fall
     *          between two consecutive occurence of the delimiter.
     *          If there is no occurence of the delimiter, it should
     *          return an array of size 1 with the string at element 0
     */
    public static String [] split(String str, char delimiter){
        String lst [] = new String [str.length()];
        String mot = "";
        int counter =0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i)!= delimiter){
                mot+=str.charAt(i);
            }else{
                lst[i]=mot;
                counter+=1;
                mot = "";
            }
        }
        lst[str.length()-1]=mot;

        String [] listed = new String [counter+1];
        int indice = 0;
        for (int i = 0; i < lst.length; i++) {
            if (lst[i]!=null){
                listed[indice]=lst[i];
                indice+=1;
                if (indice == listed.length){break;}
            }
        }
        return listed;
    }




    /**
     * Find the first occurence of a substring in a string
     *
     * @param str The string to look in
     * @param sub The string to look for
     * @return The index of the start of the first appearance of
     *          the substring in str or -1 if sub does not appear
     *          in str
     */
    public static int indexOf(String str, String sub){
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i)==sub.charAt(0)){
                if (str.substring(i, i+sub.length()).equals(sub)){
                    return i;
                }
            }
        }
        return -1;
    }


    /**
     * Convert a string to lowercase
     *
     * @param str The string to convert
     * @return A new string, same as str but with every
     *          character put to lower case.
     */
    public static String toLowerCase(String str){
        String alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String alphabetLower = "abcdefghijklmnopqrstuvwxyz";
        String res = "";
        for (int i = 0; i < str.length(); i++) {
            for (int j = 0; j<alphabetUpper.length(); j++) {
                if (alphabetUpper.charAt(j)==(str.charAt(i))||alphabetLower.charAt(j)==(str.charAt(i))) {
                    res += alphabetLower.charAt(j);
                }else if (str.charAt(i)==' '){
                    res +=' ';
                    break;
                }
            }
        }return res;

    }


    /**
     * Check if a string is a palyndrome
     *
     * A palyndrome is a sequence of character that is the
     * same when read from left to right and from right to
     * left.
     *
     * @param str The string to check
     * @return true if str is a palyndrome, false otherwise
     */
    public static boolean palindrome(String str){
        String motReverse = "";
        for (int i = str.length()-1; i >= 0 ; i--) {
            motReverse+=str.charAt(i);
        }
        if (str.equals(motReverse)){
            return true;
        }
        else return false;
    }


}