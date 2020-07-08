public class demo02runable {

    public static void main(String[] args) {
    // 3 创建runable的对象
    runableImp imp = new runableImp();
    // 4. 创建线程对象，构造方法中传递runable接口的实现类对象
    Thread t = new Thread(imp);

    // 5, 调用start
    t.start();

    // 主线程
    for(int i = 1; i < 10; i++) {
        System.out.println(Thread.currentThread().getName() + i);
    }
    
    }
}