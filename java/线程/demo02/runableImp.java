// 1. 创建runable的实现类
public class runableImp implements Runnable{
    // 2. 重写run方法
    @Override
    public void run() {
        for(int i = 1; i < 10; i++) {
            System.out.println(Thread.currentThread().getName() + i);
        }
    }
}