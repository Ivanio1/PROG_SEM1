package files;

public class house {


    public String name = "ДОМ";

    public void add_story() {
        System.out.println("К истории присоединяется дом! ");
    }

    public static class roof {
        public String roof_name = "Крыша";

        @Override
        public int hashCode() {
            return roof_name.length();
        }
    }

    public static class pipe {
        public String pipe_name = "pipe";

        @Override
        public int hashCode() {
            return pipe_name.length();
        }
    }

    public void add_item(Object obj) {
        if (obj.hashCode() == 4) {
            System.out.println("В доме есть - труба. ");
        } else {

            System.out.println("В доме есть - крыша. ");
        }
    }

}
