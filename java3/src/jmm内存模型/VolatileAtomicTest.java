package jmm内存模型;

public class VolatileAtomicTest {

    // join()等待当前线程执行完，

    public static volatile int num = 0;

    public static void increase() {
        num ++;
    }

    public static void main(String[] args) throws InterruptedException {
        Thread[] threads = new Thread[10];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(new Runnable() {
                @Override
                public void run() {
                    for (int i = 0; i < 1000; i++) {
                        increase();
                    }
                }
            });
            threads[i].start();
        }

        for (Thread t: threads) {
            t.join();
        }

        System.out.println(num);    // <= 1000*10
    }
}
