import java.util.Arrays;

public class IntroductionExercises {

    public static int variable = 0;
    public static int[] squares;

    public static void main(String[] args) {
        attribute (5);
        System.out.println(variable);
        System.out.println(add(7,2));
        System.out.println(equalsIntegers(2,2));
        System.out.println(middleValue(1,-40,7));
        System.out.println(max(25,4));
        System.out.println(greetings("Evening"));
        int [] a = {3,7,0,9,20,3};
        int [] b = {3,7,1};
        int [] c = {3,7,0,9,20};
        System.out.println(Arrays.toString(lastFirstMiddle(a)));
        System.out.println(Arrays.toString(lastFirstMiddle(b)));
        System.out.println(Arrays.toString(lastFirstMiddle(c)));
        int [] array = {1,2,3,4,5};
        System.out.println(sum(array));
        int [] arrays = {1,12,0,30,15,6,23};
        System.out.println(maxArray(arrays));


        squares = new int[args.length];
        for(int i=0;i<args.length;i++){
            try {
                squares[i] = Integer.parseInt(args[i]) * Integer.parseInt(args[i]);
            }
            catch (NumberFormatException e){
                squares[i]=0;
            }
        }
        System.out.println(Arrays.toString(squares));


    }

    public static void attribute(int value){
        variable = value;
    }

    public static int add(int a, int b){
        return (a+b);
    }

    public static boolean equalsIntegers(int a, int b) {
        if (a == b) {
            return true;
        }
        else{ return false;}
    }

    public static int middleValue(int a, int b, int c){
        if (a<b && b<c||c<b && b<a){
            return b;
        }
        else if (b<a && a<c || c<a && a<b){
            return a;
        }
        else if (b<c && c<a || a<c && c<b){
            return c;
        }
        return -1;
    }

    /*
     * Function that returns the max between a and b
     * You must use a ternary operation
     */
    public static int max(int a, int b){
        int maxi = (a>b)? a:b;
        return maxi;
    }

    public static String greetings(String str) {

        switch (str) {
            case "Morning":
                return "Good morning, sir!";
            case "Evening":
                return "Good Evening, sir!";
            default:
                return "Hello, sir!";
        }
    }

    public static int [] lastFirstMiddle(int[] a) {
        int [] lst =new int [3];
        lst[0] = a[a.length-1];
        lst[1] = a[0];
        lst[2] = a[a.length/2];
        return lst;
    }

    public static int sum(int[] array) {
        int sum = 0;
        for(int i=0;i<array.length;i++){
            sum+=array[i];
        }
        return sum;

    }

    public static int maxArray(int[] array)  {
        int i=1;
        int maximum = array[0];
        while (i<array.length){
            if (array[i]>maximum){
                maximum = array[i];
            }
            i++;
        }
        return maximum;
    }


}
