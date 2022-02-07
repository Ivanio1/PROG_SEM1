package files;
public class Bottle {
    public void full(int n){
        if (n==0){
            System.out.println("бутылка полная ");
        }else {
            System.out.println("бутылка пустая ");
        }
    }
    public String name(){
        return "бутылку";
    }
}


