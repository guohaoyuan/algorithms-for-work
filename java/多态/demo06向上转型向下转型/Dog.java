public class Dog extends Animals {

    // 重写父类的抽象方法
    @Override 
    public void method() {
        System.out.println("狗吃骨头。。");
    }

    public void Watch() {
        System.out.println("狗看家..");
    }
}