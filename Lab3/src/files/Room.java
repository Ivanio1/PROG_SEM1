package files;

public class Room {
    public void add_item(Object obj) {
        if (obj instanceof Car) {
            System.out.println("В комнате есть - машина. ");
        }
        if (obj instanceof Spirtovka) {
            System.out.println("В комнате есть - спиртовка. ");
        }
        if (obj instanceof Bottle) {
            System.out.println("В комнате есть - бутылка. ");
        }
        if (obj instanceof item && ((item) obj).be()==0) {
            System.out.println("В комнате есть - окно и подоконник. ");
        }
        if (obj instanceof item && ((item) obj).be()==1) {
            System.out.println("В комнате есть - тряпка. ");
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Car) return true;
        else return false;
    }
}



