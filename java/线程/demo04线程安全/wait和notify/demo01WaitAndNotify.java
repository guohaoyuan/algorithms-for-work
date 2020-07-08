public class demo01WaitAndNotify {

    public static void main(String[] args) {
        // 创建锁对象，保证唯一
        Object l = new Object();

        new Thread() {
            @Override
            public void run() {
                // 利用同步代码块
                while(true) {
                    synchronized(l) {
                        System.out.println("消费者：我要吃包子！");

                        // 可能发生异常的代码
                        try {
                            // 进入休眠状态
                            l.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }

                        // 被唤醒后，真香
                        System.out.println("消费值吃包子：真香！");
                        System.out.println("----------------");
                    }
                    
                }

            }
        }.start();

        // 创建生产者线程
        new Thread() {
            @Override
            public void run() {
                while(true) {
                    System.out.println("生产者得到消费者信息，花5秒做包子！");
                    
                    // 可能发生异常的代码
                    try {
                        Thread.sleep(5000);
                    } catch (Exception e) {
                        //TODO: handle exception
                        e.printStackTrace();
                    }
                    synchronized(l) {
                        l.notify();
                        System.out.println("生产者做好包子");
                        System.out.println("......");
                    }
                    
                }
            }
        }.start();
    }
}