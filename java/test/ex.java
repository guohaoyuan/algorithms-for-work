import java.lang.reflect.Method;

public class ex {


    public static void main(String[] args) {
        dog d1 = new dog();
        dog d2 = new dog();
        System.out.println(d1 == d2);
        System.out.println(d1.equals(d2));
    }
}