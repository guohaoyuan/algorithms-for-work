package 泛型;

public class demo05test {
    public static void main(String[] args) {
        demo05interim<String> impl1 = new demo05interim<>();
        impl1.method("aaa");

        demo05interim<Integer> impl2 = new demo05interim<>();
        impl2.method(111);
    }
}
