public class test {
    public static String name;

    public static void main(String[] args) {
        int x=1;
        x+=x++ + ++x;
        System.out.println(x);
    }
}