import java.lang.reflect.Array;
import java.util.Arrays;

public class ArraySorter {
    public static void main(String[] args){
        Sort(5);
    }
    public static void Sort(int n){
        int[] a = new int[n];
        for (int i=0;i<n;i++){
            a[i]=(int)(Math.random()*10);
        }
        Arrays.sort(a);
        for (int i=0;i<n;i++){
            System.out.println(a[i]);
        }
    }
}
