package 抽象类.demo01抽象类的实现;

/**
 * abstract修饰的方法是抽象方法，所在的类必须是抽象类。
 * 抽象方法没有方法体，因为在父类中具体实现不确定
 *
 * 如何使用：
 *      1. 必须用子类继承抽象类，并重写其中所有的抽象方法。
 *      2. 创建子类对象进行使用
 */
public abstract class Animal {

    // 具体实现还不清除
    public abstract void eat();

    // 抽象类中可以有普通方法
    public void normalMethod() {

    }
}
