public class ingi 
{
    public static void main(String []args)
    {
        /* 1*/

        int heure = 22;
        int minute =  14;
        int seconde = 12;
        int total = 0;

        total= (heure*3600 + minute*60 + seconde);
        System.out.println(total+"s");

        System.out.println(IMC(1.30,100));

        System.out.println(ordonne(6,4,5));

        


       
    }

    /* 2 */

    public static double IMC(double taille, int poids)
    {
       
        double imc  = (poids/(taille*taille));
        if (imc<20)
        {
            System.out.println("Mince");
            return imc;
        }

        else if (imc>=20 && imc<=25)
        {
            System.out.println("Noraml");
            return imc;
        }

        else if (imc>25 && imc<=30)
        {
            System.out.println( "embonpoint");
            return imc;
        }

        else 
        {
            System.out.println( "Obèse");
            return imc;
        }
    }

    /* 3 */

    public static boolean ordonne(int a , int b, int c)
    {
        if (a<b&&b<c)
        {
            return true;
        }

        else 
        {
            return false;
        }
    }


}
