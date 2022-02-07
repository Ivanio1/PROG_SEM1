package files;

public class Karlson extends Person implements be_the_greatest, be_proud {
    public int height = 10;
    public int speed = 5;

    public Karlson(String name, String gender, String condition) {
        super(name, gender, condition);
    }

    public void go_through_window() {
        System.out.println(name + " быстро перекинул через подоконник одну за другой свои маленькие толстенькие ножки и очутился в комнате.");
    }

    public void change_height(int n, int r) {
        int h = this.height;
        for (int i = 1; i < n; i++) {
            h = h + r;
        }
        if (h > this.height) {
            System.out.println(name + " набирает высоту. ");
        } else {
            System.out.println(name + " снижает высоту. ");
        }
    }

    public void change_speed(int n, int r, Object obj) {
        int h = this.height;
        for (int i = 1; i < n; i++) {
            h = h + r;
            if (h < 0) {
                throw new WrongSpeed();
            }
        }
        if (obj instanceof BabyBoy) {
            if (h > this.height) {
                System.out.println(name + " прибавляет скорость и проносится мимо " + ((BabyBoy) obj).getName() + ", как настоящий самолёт. ");
            } else {
                System.out.println(name + " снижает скорость. ");
            }
        }
    }

    public void make_circles(int n) {
        int r = n;
        for (int i = 0; i < n; i++) {
            System.out.println(name + " сделал " + (r) + " круг.");
            r++;
        }
    }


    public void fly() {
        System.out.println(" полетел.");
    }

    public void fly_around(Object obj) {
        if (obj instanceof house.roof) {
            System.out.println(name + " облетел вокруг крышы. ");
        }
        if (obj instanceof house.pipe) {
            System.out.println(name + " облетел вокруг трубы. ");
        }

    }


    @Override
    public void grab(Object obj) {
        if (obj instanceof Bottle) {
            System.out.println(name + " схватил бутылку. ");
        }
        if (obj instanceof Car) {
            System.out.println(name + " вытащил стоявшую там игрушечную паровую машину. ");
        }
    }

    @Override
    public void pour(Spirtovka spitovka) {
        System.out.println(name + " успешно налил денатурат в" + spitovka.name() + "и зажёг фитиль.");
    }

    public int burn(int n) {
        if (n == 0) {
            System.out.println("Карлсон сумел налить денатурат и не разлил его! Ура! ");
            return 0;
        } else {
            System.out.println(name + " неуклюже наливал и пролил денатурат! ");
            return 2;
        }
    }

    @Override
    public int shout(int n) {
        return n;
    }

    @Override
    public void jump(int n) {
    }

    @Override
    public void kneel_down() {
        System.out.print(name + " опустился на колени возле паровой машины, ");
    }

    public void eyes_glittered() {
        System.out.println(" глаза заблестели.");
    }

    @Override
    public void stand() {

    }

    @Override
    public void waiting() {

    }

    @Override
    public void look_at(Object object) {
        if (object instanceof BabyBoy) {
            System.out.print(name + " окинул " + ((BabyBoy) object).getName() + " внимательным, долгим взглядом и");
        } else {
            System.out.println("Карлсон не увидел Малыша! ");
        }
    }

    public void walk_to() {
        System.out.print(name + " подошёл к книжной полке Малыша и ");
    }

    @Override
    public void be_the_greatest() {
        System.out.println(name + " был лучшим в мире специалистом по паровым машинам.");
    }



    @Override
    public void be_proud() {
        System.out.println(name + " выглядел таким гордым и счастливым, будто сам её изобрёл.");
    }
}

