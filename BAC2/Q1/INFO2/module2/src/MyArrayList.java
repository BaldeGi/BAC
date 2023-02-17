import java.util.*;


public class MyArrayList<Item> implements Iterable<Item> {

    private Object [] list;
    private int size;

    public static void main(String[] args) {
        MyArrayList<Integer> list = new MyArrayList<>(1);
        list.enqueue(1);
        list.enqueue(2);
        list.enqueue(3);
        list.enqueue(4);
        list.enqueue(5);
        list.remove(1);
        Iterator ite = list.iterator();
        ite.hasNext();
        System.out.println(ite.next());
        ite.hasNext();
        ite.hasNext();
        ite.hasNext();
        System.out.println(ite.next());
        System.out.println(ite.next());
        System.out.println(ite.next());
        System.out.println(Arrays.toString(list.getList()));

    }



    public MyArrayList(int initSize){
        if(initSize<1) throw new IndexOutOfBoundsException();
        this.size = 0;
        this.list = new Object[initSize];
    }


    /*
    * Checks if 'list' needs to be resized then add the element at the end 
    * of the list.
    */
    public void enqueue(Item item){
        if (size()>=list.length){
            resize();
        }
        getList()[size] = item;
        size++;
    }

    public void resize(){
        Object [] res = new Object[size*2];
        for (int i = 0; i < size; i++) {
            res[i] = list[i];
        }
        list = res;
    }


    /*
    * Removes the element at the specified position in this list.
    * Returns the element that was removed from the list. You dont need to 
    * resize when removing an element.
    */
    public Item remove(int index){
        if(index<0||index> list.length-1) throw new IndexOutOfBoundsException();
        int count =0;
        Object [] array = new Object[list.length];
        int j = 0;
        for (int i = 0; i < list.length; i++) {
            if(list[i]!=null) {
                array[j] = list[i];
                count++;
                j++;
            }
        }

        Object [] arrays = new Object[count];
        count=0;

        Item item = (Item) array[index];
        array[index] = null;

        j=0;
        for (int i = 0; i < array.length; i++) {
            if(array[i]!=null) {
                arrays[j] = array[i];
                count++;
                j++;
            }
            else count++;
        }

        list = arrays;
        size=arrays.length-1;
        return item;
    }


    public int size(){
        return this.size;
    }
    
    
    public Object [] getList(){
        return this.list;
    }


    @Override
    public Iterator<Item> iterator() {
        return new MyArrayListIterator();
    }


    private class MyArrayListIterator implements Iterator<Item> {
        int index = MyArrayList.this.size;
        int i = 0;
        @Override
        public boolean hasNext() {
            if(index!=size){
                throw new ConcurrentModificationException();
            }
            return i< size;
        }


        @Override
        public Item next() {
            if(hasNext()){
                Item item = (Item) getList()[i++];
                return item;
            }

            else{throw new NoSuchElementException();}
        }
        // YOUR CODE HERE
    }

}