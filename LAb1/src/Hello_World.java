public class Hello_World {
    public static void main(String[] args){
        int i =0;
        switch (args.length){
            case 0:
                System.out.println("Hello, world!");
                break;
            default:
                while (i< args.length){
                    System.out.println("Hello, " + args[i]+". Your name is "+args[i].length()+" letters long!");
                    i++;
                }
        }
    }
}
