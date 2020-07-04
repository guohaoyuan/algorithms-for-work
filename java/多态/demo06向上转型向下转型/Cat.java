public class Cat extends Animals{

    // 重写父类方法override
    @Override
    public void method() {
        System.out.println("猫吃鱼。。。");
    }

    public void CatchMouse() {
        System.out.println("猫抓老鼠。。。");
    }
}