package 泛型;

public class demo05interim<T> implements demo05interface<T> {
    @Override
    public void method(T t) {
        System.out.println(t);
    }
}
