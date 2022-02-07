package files;

public class BabyBoy extends Person implements be_afraid, took_a_breath_away,be_afraid_of_fire{
    public BabyBoy(String name, String gender, String condition) {
        super(name, gender, condition);
    }
    public int fight_fire(){
        System.out.print("и прибил пламя");
        return 1;
    }
    @Override
    public void grab(Object obj) {
        if (obj instanceof Bottle){
            System.out.println(name + " схватил бутылку. ");}
        if (obj instanceof Rag){
            System.out.print(name + " схватил тряпку ");}
    }

    @Override
    public void pour(Spirtovka spitovka) {
    }

    @Override
    public int be_afraid(int n) {
        if (n==1) {
            System.out.println(name + " испуган. ");
            return 1;
        }else{return 0;}}



    @Override
    public int shout(int n) {
        if (n == 1) {
            System.out.print(name + " всрикнул и");
            return 1;
        }
        return 0;
    }

    @Override
    public void jump(int n) {
        if (n == 1) {
        System.out.print(" отскочил. ");
    }
    }

    @Override
    public void kneel_down() {

    }

    @Override
    public void stand() {
        System.out.println(name+" стоял не шелохнувшись. ");
    }

    @Override
    public void waiting() {
        System.out.println(name+" и ждал, что будет дальше. ");
    }

    @Override
    public void look_at(Object object) {
    }


    public String getName() {
        return name;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof BabyBoy) {
            return name.equals(((BabyBoy) obj).getName());
        } else return false;
    }


    @Override
    public int breath() {
        System.out.println("У него просто дух захватило от волнения.");
        return 1;
    }

    @Override
    public void fire() {
        System.out.println(name+" не мог стоять спокойно, когда видел огонь.");
    }
}
