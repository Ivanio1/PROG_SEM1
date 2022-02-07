
package files;
public class Denaturat {
    public int condition(int n) {
        if (n == 1) {
            System.out.println("Денатурат в бутылке.");
        } else if (n == 2) {
            System.out.println("Денатурат на поверхности. Образовалось большое озеро. ");
        } else if (n == 3) {
            System.out.println("Денатурат в спиртовке.");
        } else if (n==0){
            System.out.println("Денатурат исчез!!");
        }
        return n ;
    }
}

