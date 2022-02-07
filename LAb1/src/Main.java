
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int [] arr=new int[num];
        for (int i =0;i<num;i++){
            arr[i]=i+1;
        }
        for (int i=0;i<num;i++)
            System.out.print(arr[i]+" ");

    }
}
