package 内部类;

public class demo01InnerClass {

    public static void main(String[] args) {
        Body body = new Body(); // 外部类对象
        // 通过外部类对象，调用内部类的方法，里面间接使用在内部类Heart
        body.methodBody();
        System.out.println("===============");

        // 直接使用内部类的对象调用内部类方法
        Body.Heart heart = new Body().new Heart();
        heart.beat();
    }
}
