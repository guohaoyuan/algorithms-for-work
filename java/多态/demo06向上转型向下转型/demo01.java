/**
 * 一旦向上转型为父类，一定安全，但是有一个缺点：无法调用子类特有方法
 * 
 * 解决方法：利用向下转型，进行还原
 */
public class demo01 {

    public static void main(String[] args) {
        // 向上转型，就是父类引用，指向子类对象
        Animals animal  = new Cat();    // 本来是猫，向上转型为animals
        animal.method();
        // 编译看左，执行看右

        // animal.CatchMouse();    // 错误写法
        Cat cat = (Cat) animal;
        cat.CatchMouse();

        Dog dog = (Dog) animal; // 原本是一只猫，非要向下转型为狗，报错classCast异常
        // 编译不会报错，但是会出异常
    }
}