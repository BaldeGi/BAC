import java.util.ArrayList;
import java.util.Arrays;

public class Decoder {

    public static void main(String[] args) {
        StringBuilder builder = new StringBuilder(" ");
        builder.append("ab");
        System.out.println(builder);
        String[][] input = new String[][]{{"084", "104", "105", "115", "032", "105", "115", "032"},
                {"097", "032", "108", "097", "114", "103", "101", "114"},
                {"115", "101", "116", "032", "111", "102", "032", "115", "101", "110",
                        "116", "101", "110", "099", "101", "115", "046", "046", "046"}};
        int[] forbid = new int[]{32, 101};
        System.out.println(Arrays.toString(decode(forbid, input)));
        ArrayList<Character> buld = new ArrayList<>();
        System.out.println(buld);


        int f = (char) 011;
        char g = (char) 117;
        char h = (char) 79;
        char i = (char) 032;


        System.out.println(f);
        System.out.println(g);
        System.out.println(h);
        System.out.println(i);


    }

    /**
     * Forbidden characters are passed as an array of int.
     * Each element of this array correspond to the decimal ASCII code
     * of a forbidden character OR null if there's no forbidden character
     * If you encounter one of these forbidden character
     * you must ignore it when you translate your sentence.
     * <p>
     * the 2D array "sentences" contain a set of decimal ASCII code we want you
     * to translate. Each sub-element of this array is a different sentence.
     * Ex : if we pass this array : [ ["42", "72", "88"], ["98", "99", "111", "47", "55"]]
     * to your decode method, you should return : [ "*HX", "bco/7" ]
     * <p>
     * You should NEVER return null or an array containing null
     **/
    public static String[] decode(int[] forbidden, String[][] sentences) {
        ArrayList<Character> list = new ArrayList<>();
        if (forbidden != null) {
            for (int i = 0; i < forbidden.length; i++) {
                char a = (char) forbidden[i];
                list.add(a);
            }
        }
        ArrayList<Character> forbiddenList = list;
        String[] res = new String[sentences.length];
        for (int i = 0; i < sentences.length; i++) {
            String builder = "";
            for (int j = 0; j < sentences[i].length; j++) {
                int a = Integer.parseInt(sentences[i][j]);
                char b = (char) a;
                if (forbiddenList != null && forbiddenList.contains(b)) {
                    continue;
                } else {
                    builder += b;
                }
            }
            res[i] = builder;
        }
        return res;
    }
}




