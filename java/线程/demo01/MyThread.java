
// 1. 继承线程
public class MyThread extends Thread{

    // 2. 重写run方法
    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println("thread" + i);
        }
    }

}