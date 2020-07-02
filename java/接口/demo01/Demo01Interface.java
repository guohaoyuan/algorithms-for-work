/**
 * 接口就是一个多类的公共规范。
 * 接口是一种引用数据类型，最重要的：抽象方法
 * 
 * 如何定义一个接口格式
 * public interface 接口名称 {
 *      // 接口内容
 * }
 * 
 * 对于java 10
 * 1. 常量
 * 2. 抽象方法
 * 3. 默认方法
 * 4. 静态方法
 * 5. 私有方法
 * 
 * 使用步骤：
 * 1. 接口不能直接使用， 必须有一个实现类来实现接口
 * 
 * 格式：
 * public class 实现类名称 implements 接口名称 {
 *  
 * }
 * 
 * 2. 接口的实现类必须覆盖重写接口中所有抽象方法
 * 去掉abstract, 加上方法体大括号
 * 
 * 3. 实现类的对象进行使用
 * 
 * 
 * note:
 * 如果实现类没有覆盖重写接口中所有的抽象方法， 那么这个实现类自己就必须是抽象类 
 */

 public class Demo01Interface {
     
    public static void main(String[] args) {
        // 实现类的对象使用
        MyImp1 imp1 = new MyImp1();
        imp1.methodAbs1();
        imp1.methodAbs2();
    }
 }