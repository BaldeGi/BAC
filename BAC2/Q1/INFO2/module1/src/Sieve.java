import java.util.BitSet;

public class Sieve {

    public static void main(String[] args) {
        System.out.println(numberOfPrime(10));
    }

    public static BitSet bits; //You should work on this BitSet

    public static int numberOfPrime(int n){
        Sieve.bits = new BitSet(n);
        bits.set(2,n);
        for(int i = 2; i<=Math.sqrt(n); i++){
            if (bits.get(i)){
                for(int j = i*i; j<=n; j+=i){
                    bits.clear(j); // peut être remplacé par  bits.clear(j,false)
                }
            }
        }
        return bits.cardinality();
    }
}

