package 线程;

public class classTest {

    public static void main(String[] args) {
        Thread t1 = new Thread(new MyThread());
        t1.start();
    }
}
