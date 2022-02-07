
package files;

public abstract class Person {
    public String name=" Person ";
    public String gender=" Unknown ";
    public String condition="Default";
    public Person(String name, String gender, String condition){
       this.name=name;
       this.gender=gender;
       this.condition=condition;
    }
    @Override
    public String toString(){
        if (gender.equals("male")) {
            System.out.println(name + " присоединился к истории. ");
        }
        else {
            System.out.println(name + " присоединилась к истории. ");
        }
        return null;
    }
    public abstract void grab(Object obj);
    public abstract void pour(Spirtovka spitovka);
    public abstract int shout(int n);
    public abstract void jump(int n);
    public abstract void kneel_down();
    public abstract void stand();
    public abstract void waiting();
    public abstract void look_at(Object object);
}

