import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class demo01ThreadPool {

    public static void main(String[] args) {
        // 1. 使用线程池的工厂类Executors里面提供的newFixedThreadPool生产一个指定线程数量的线程池
        ExecutorService es = Executors.newFixedThreadPool(2);

        // 线程池一直开启，使用完线程，会自动归还线程，可以重复使用
        es.submit(new RunnableImpl());
        es.submit(new RunnableImpl());
        es.submit(new RunnableImpl());

    }
}