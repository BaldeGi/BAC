import java.util.ArrayList;
import java.util.Iterator;

public class MakeMistakeToUnderstandThem {

    public static void main(String[] args) {


	String[] names = { "tom", "bob", "harry" };
	for (int i = 0; i <= names.length; i++) {
	    System.out.println(names[i]);
	}
	 
	 
	 
	       
        String str = null;
        System.out.println(str.toUpperCase());
        
        
        
        

	ArrayList<Integer> list = new ArrayList<>();

	list.add(1);
	list.add(2);
	list.add(3);
	list.add(4);
	list.add(5);

	Iterator<Integer> it = list.iterator();
	while (it.hasNext()) {
	    Integer value = it.next();
	    System.out.println("List Value:" + value);
	    if (value.equals(3)){
		list.remove(value);
	    }

       }

    } 
}
