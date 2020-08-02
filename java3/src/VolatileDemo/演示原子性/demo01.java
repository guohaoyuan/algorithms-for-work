package VolatileDemo.演示原子性;

import java.util.concurrent.atomic.AtomicInteger;

class data {
    volatile int number = 0;

    public void addPuls() {
        this.number++;
    }

    AtomicInteger atomicInteger = new AtomicInteger();

    public void myaddAtomic() {
        atomicInteger.getAndIncrement();
    }
}
public class demo01 {

    public static void main(String[] args) {
        data d = new data();

        for(int i = 1; i <= 20; i++) {
            new Thread(() -> {
                for(int j = 1; j <= 1000; j++) {
                    d.addPuls();
                    d.myaddAtomic();
                }
            }, String.valueOf(i)).start();

        }

        while(Thread.activeCount() > 2) {
            Thread.yield();
        }

        System.out.println("main, the number is " + d.number);
        System.out.println("main, the atomicInteger is " + d.atomicInteger);
    }
}
