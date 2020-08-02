package 死锁;

public class deadLockDemo {
    private static final Object a = new Object();
    private static final Object b = new Object();


    public static class Task implements Runnable {

        private boolean flag;

        public Task(boolean flag) {
            this.flag = flag;
        }

        @Override
        public void run() {
            if(flag) {
                synchronized (a) {
                    System.out.println(Thread.currentThread().getName() + "-> 获取到锁a");

                    synchronized (b) {
                        System.out.println(Thread.currentThread().getName() + "-> 获取锁b");
                    }
                }
            } else {
                synchronized (b) {
                    System.out.println(Thread.currentThread().getName() + "-> 获取到锁b");

                    synchronized (a) {
                        System.out.println(Thread.currentThread().getName() + "-> 获取锁a");
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        // 如果第一个线程已经走完，第二个线程才能取到执行权限，那么就不会出现死锁
        new Thread(new Task(true)).start();
        new Thread(new Task(false)).start();
    }
}
