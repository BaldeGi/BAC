
public class LearnExceptionInJava{

    /*
     * This method receives two integer as argument and return the exact result of the division i1/i2
     * It should throw an ArithmeticException if the second integer is equal to 0
     * */

    public static void main(String[] args) {
        System.out.println(divide(4,2));
        System.out.println(canDivide(4,2));
        System.out.println(betterDivide(4,2));
        System.out.println(betterCanDivide(4,0));
    }

    public static double divide(int i1, int i2) throws ArithmeticException{
        //TODO by student
        if (i2==0)
            throw new ArithmeticException("Impossible de faire une division par Zero");
        else {
            double res= (double) i1/i2;
            return res;
        }
    }

    public static boolean canDivide(int i1, int i2){
        //Your code here
        try{
            divide(i1,i2);
            return true;
        }
        catch (Exception e){
            return false;
        }
    }

    public static double betterDivide(int i1, int i2) throws ArithmeticException {
        //Your code here
        if (i2 == 0)
            throw new ArithmeticException("You tried to divide by zero");
        else {
            double res = (double) i1 / i2;
            return res;
        }
    }

    public static String betterCanDivide(int i1, int i2){
        //Your code here
        try{
            double res = betterDivide(i1,i2);
            return String.valueOf(res);
        }
        catch (ArithmeticException e){
            return "You tried to divide by zero";
        }
    }

}