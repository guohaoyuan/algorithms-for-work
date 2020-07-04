/**
 * 为了避免向下转型出错，如何判断父类引用的对象，原本的子类对象是谁？
 * 
 * 解决防范instanceof
 * 对象名称 Instanceof 类名
 * 得到一个布尔值，判断前面的对象是否为后面类的实例
 */
public class demo01Main {

    public static void main(String[] args) {

        Animals animal = new Cat();    // 向上转型

        // 对象名 instanceof 类名
        if (animal instanceof Dog) {
            Dog dog = (Dog) animal; // 向下转型， 先判断父类引用对象属于哪个类
            dog.Watch();
        }

        if (animal instanceof Cat) {
            Cat cat = (Cat) animal;
            cat.CatchMouse();
        }

        // 关于有什么用， 看着很繁琐， 当传入的对象不明确时，有用。
        // 例如不清楚传入的动物是猫还是狗
        GiveMeAPet(new Dog());
        GiveMeAPet(new Cat());
    }

    public static void GiveMeAPet(Animals animal) {
        if (animal instanceof Dog){
            Dog dog = (Dog) animal;
            dog.Watch();
        }

        if (animal instanceof Cat) {
            Cat cat = (Cat) animal;
            cat.CatchMouse();
        }
    }
}