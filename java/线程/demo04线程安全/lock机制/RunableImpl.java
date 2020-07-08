import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class RunableImpl implements Runnable {
    // 定义一个多线程共享的资源
    private int ticket = 100;

    // 1 在成员位置定一个锁对象
    Lock l = new ReentrantLock();

    // // 重写run方法
    // @Override
    // public void run() {
    //     while(true) {
    //         // 2 在可能出现线程安全前加锁
    //         l.lock();
    //         // 判断票是否存在
    //         if(ticket > 0) {
    //             try {
    //                 Thread.sleep(10);
    //             } catch (InterruptedException e) {
    //                 e.printStackTrace();
    //             }

    //             // 票存在ticket--
    //             System.out.println(Thread.currentThread().getName() + "正在卖" + ticket + "张票");
    //             ticket--;
    //         }
    //         // 3 在线程安全代码后解锁
    //         l.unlock();
    //     }
    // }



    // 重写run方法
    @Override
    public void run() {
        while(true) {
            // 2 在可能出现线程安全前加锁
            l.lock();
            // 判断票是否存在
            if(ticket > 0) {
                try {
                    Thread.sleep(10);
                    // 票存在ticket--
                    System.out.println(Thread.currentThread().getName() + "正在卖" + ticket + "张票");
                    ticket--;
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } finally {
                    // 3 在线程安全代码后解锁
                    l.unlock();
                }

                
            }
            
        }
    }


}