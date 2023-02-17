import java.sql.Array;
import java.util.*;

public class Person {
    public String name;
    public int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return name + " " + age;
    }

    public static void main(String[] args) {
        ArrayList<Person> persons = new ArrayList<>();
        persons.add(new Person("Guillaume",20));
        persons.add(new Person("John",50));
        persons.add(new Person("Guillaume",10));
        persons.add(new Person("John",10));
        persons.add(new Person("Luc",5));

        sortPerson(persons);
        System.out.println(persons);



    }

    public static void sortPerson(ArrayList<Person> persons) {
        Comparator<Person> c = (o1, o2) -> {
            if (o1.name==o2.name){
                return (o1.age-o2.age);
            }else{
                return (o1.name.compareTo(o2.name));
            }
        };
        persons.sort(c);

    }

}
