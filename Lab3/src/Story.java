import files.*;
public class Story {
    public static void main(String[] args) throws KarlsonIsNotReadyToFly {
        Karlson Vasya = new Karlson("МУЖЧИНА В РАСЦВЕТЕ СИЛ","male", "healthy");
        BabyBoy boy=new BabyBoy("Малыш","male","healthy");
        if (Vasya.condition.equals("healthy")) {
            System.out.println("Начало истории.");
        } else {
            throw new KarlsonIsNotReadyToFly("Карслон болеет. Попробуйте позже.");}
        Vasya.toString();
        boy.toString();
        System.out.println("");
        Vasya.look_at(boy);
        Vasya.fly();
        Vasya.change_height(5,1);
        Vasya.make_circles(1);
        house h=new house();
        house.pipe truba = new house.pipe();
        house.roof krysha = new house.roof();
        h.add_story();
        h.add_item(truba);h.add_item(krysha);
        Vasya.fly_around(truba);
        Vasya.change_speed(3,1,boy);
        Vasya.make_circles(2);
        System.out.println("");
        Goosebumps bumps = new Goosebumps(Goosebumps_place.back);
        boy.stand();boy.waiting();
        bumps.run(boy.breath(),bumps);
        Room room=new Room();
        item window = new item() {
            @Override
            public int be() {
                return 0;
            }
        };

        System.out.println("");
        room.add_item(window);
        Vasya.go_through_window();
        Car car = new Car(Car_status.Stand);
        if (room.equals(car)){
        room.add_item(car);
        car.rotation(car);}
        Vasya.walk_to();Vasya.grab(car);

        //
        System.out.println("");
        Spirtovka spirtovka = new Spirtovka("спиртовка");
        Bottle bottle = new Bottle();
        Denaturat den = new Denaturat();
        room.add_item(spirtovka);
        room.add_item(bottle);
        den.condition(1);
        Vasya.pour(spirtovka);
        Vasya.be_the_greatest();
        Flame_boys boys= new Flame_boys();
        boy.jump(boy.shout(boy.be_afraid(boys.danse(den.condition(Vasya.burn(1))))));
        //
        System.out.println("");
        big_ugly_spots spots=new big_ugly_spots();
        item rag = new item() {
            @Override
            public int be() {
                return 1;
            }
        };
        room.add_item(rag);
        boy.fire();spots.be_on_surface(boy.fight_fire());
        Vasya.kneel_down();Vasya.eyes_glittered();
        car.setStatus(Car_status.Work);
        car.rotation(car);
        car.be_the_greatest();
        Vasya.be_proud();

    }
}
