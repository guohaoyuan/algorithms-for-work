public class RunableImpl implements Runnable {
    // 定义一个多线程共享的资源
    private static int ticket = 100;

    // 创建一个锁对象
    Object lock = new Object();

    // 重写run方法
    @Override
    public void run() {
        while(true) {
            // 使用同步代码块
            method();
        }
    }

    public static synchronized void method() {
        // 判断票是否存在
        if(ticket > 0) {
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            // 票存在ticket--
            System.out.println(Thread.currentThread().getName() + "正在卖" + ticket + "张票");
            ticket--;
        }
    }
}