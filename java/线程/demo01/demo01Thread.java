public class demo01Thread {

    public static void main(String[] args) {
        // 3. 创建线程对象
        MyThread mt = new MyThread();

        // 4/ 开始线程
        mt.start();

        for(int i = 0; i < 10; i++) {
            System.out.println("main" + i);
        }
    }

}