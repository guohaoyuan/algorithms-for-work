public class RunnableImpl implements Runnable{

    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName() + "执行新线程");
    }
}