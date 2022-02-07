import java.lang.reflect.Field;
import java.text.Annotation;

public class test{
    public static void main(String[] args){
        Field[] fields=Car.class.getDeclaredFields();
        for(int i=0;i<fields.length;i++){
            Annotation an=fields[i].getAnnotation(Resource.class);
            if(an!=null){
                System.out.println(fields[i].getName());
            }
        }
    }


}
