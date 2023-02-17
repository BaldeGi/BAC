public class training
{
    public static void main(String[] args)
    {
		System.out.println(isSameNum(23,2));
        System.out.println(myn(-955,-111,150));
        System.out.println(fonct(20,3,14,0));

        

        int i = 0;

        while(i!=10)
        {
            System.out.println(i);
            i++;
        }
        System.out.println();

        for ( i=0 ; i!=10; i++)
        {
            System.out.println(i);
        }


       

	}

    public static boolean isSameNum(int x, int y)
    {
		if(x==y)
        {
            return true;
        }

        else 
        {
            return false;
        }
	}

    public  static double myn(double a, double b , double c)
    {
        {
            double moyenne = 0;
            moyenne = (a+b+c)/3;
            return moyenne;
        }
    }  

    public static int fonct(int heure, int minute, int seconde, int total)
    {
        total =(heure*3600)+(minute*60)+(seconde);
        return total;
    }

        
}
