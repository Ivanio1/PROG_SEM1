public class Hello {
    public static void main(String[] args){
        int i =0;
        switch (args.length){
            case 0:
                System.out.println("Hello, world!");
                break;
            case 1:
                System.out.println("Hello, " + args[i]+". Your name is "+args[i].length()+" letters long!");
                i++;
                break;
            default:
                System.out.println("Enter one word");
        }
    }
}
