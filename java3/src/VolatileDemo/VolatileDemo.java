package VolatileDemo;


import java.sql.Time;
import java.util.concurrent.TimeUnit;

class MyData {
    volatile int number = 0;

    public void addTo60() {
        this.number = 60;
    }
}

/**
 * 1. int number = 0;变量没有加volatile修饰，并没有可见性
 */
public class VolatileDemo {

    public static void main(String[] args) {
        // 保证可见性
        MyData data = new MyData();

        new Thread(() -> {
            System.out.println(Thread.currentThread().getName() + "\tcome in");
            try {
                TimeUnit.SECONDS.sleep(3);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            data.addTo60();
            System.out.println(Thread.currentThread().getName() + "\tcome out");
        }).start();

        // 第二个线程是主线程
        while(data.number == 0) {
            // main线程一直在循环，直到number为60
        }

        System.out.println(Thread.currentThread().getName() + "\t mission is over, main get number is:" + data.number);

    }
}
