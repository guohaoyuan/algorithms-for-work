package DCL;

public class Singleton {
    private volatile static Singleton instance;

    private Singleton() {
        System.out.println("构造方法SingletoDemo()");
    }
    public static Singleton getInstance() {
        if(instance == null) {
            synchronized (Singleton.class) {
                if(instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }

    public static void main(String[] args) {
        Singleton.getInstance();
    }
}
