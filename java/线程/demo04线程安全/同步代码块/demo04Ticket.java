/**
 * 解决线程安全的一种方法：同步代码块
 * 格式：
 *  synchronized(锁对象) {
 *        可能出现线程安全的代码(访问了共享数据的代码)
 * }
 * 
 * 注意：
 *  1. 通过代码快中的锁对象，可以使用任意的对象
 *  2. 但是必须保证多个线程使用的锁对象是同一个
 *  3. 锁对象的作用
 *      把同步代码块锁住，只让一个线程在同步代码块中执行
 */
public class demo04Ticket {

    public static void main(String[] args) {
        RunableImpl r = new RunableImpl();
        Thread t1 = new Thread(r);
        Thread t2 = new Thread(r);
        Thread t3 = new Thread(r);
    
        t1.start();
        t2.start();
        t3.start();
    }

}