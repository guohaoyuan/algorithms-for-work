/**
 * new 接口/父类（）{
 *      重写父类/接口中的方法
 * };
 */
public class demo03InnerClassThread {

    public static void main(String[] args) {
        
    // 使用thread直接创建线程
    new Thread() {
        @Override
        public void run() {
            for(int i = 0; i < 10; i++) {
                System.out.println(Thread.currentThread().getName() + i + "GHY");
            }
        }
    }.start();

    // 使用runable创建线程
    Runnable r = new Runnable(){
    
        @Override
        public void run() {
            // TODO Auto-generated method stub
            for(int i = 0; i < 10; i++) {
                System.out.println(Thread.currentThread().getName() + i + "YY");
            }
        }
    };

    new Thread(r).start();


    // 简化runnable的写法
    new Thread(new Runnable() {

        @Override
        public void run() {
            // TODO Auto-generated method stub
            for(int i = 0; i < 10; i++) {
                System.out.println(Thread.currentThread().getName() + i + "SDASD");
            }
        }
    }).start();
    
    }

}