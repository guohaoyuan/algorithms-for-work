/**
 * 接口的默认方法，可以通过接口实现类对象， 直接调用
 * 接口的默认方法， 可以通过被接口实现类进行覆盖重写
 */
public class demo02Interface {
    
    public static void main(String[] args) {
        // 创建实现类的对象
        MyInterfaceDefaultA a = new MyInterfaceDefaultA();

        // 调用抽象方法， 实际上调用右侧的实现类
        a.methodAbs();

        // 调用默认方法， 如果实现类中没有，会向上找接口
        a.methodDefault();
        System.out.println("==============");

        MyInterfaceDefaultB b = new MyInterfaceDefaultB();

        // 调用抽象方法
        b.methodAbs();

        b.methodDefault();
    }
}