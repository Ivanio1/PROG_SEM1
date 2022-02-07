public class DefactoFIlter {
    public static void main(String[] args){
        String s="Я.не,де-факто!он?она";
        Split(s);
    }
    public static void Split(String s){
        String[] S=s.split(",|!|\\.|\\?");
        int n=0;
        for (String value : S) {
            if (value.equals("де-факто")) {
                n += 1;

            } else {
                System.out.println(value);
            }
        }
        System.out.println(n);

    }
}
