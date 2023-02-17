public class Methodes 
{
    public static void main(String []args)
    {
        prog();
        prog();
        System.out.println(getNumberTwo());
        say("Hello !",20);
    }


    public static void prog()
    {
        System.out.println("Bonjour");
        System.out.println("Comment allez-vous");
        System.out.println("Bien");
    }


    public static  int getNumberTwo()
    {
        return 2;
    }

    public static void say(String msg , int nb)
    {
        System.out.println(msg);
        System.out.println(nb);
    }

    
}
