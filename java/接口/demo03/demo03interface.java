/**
 * 不能通过接口实现实现类的对象来调用接口当中的静态方法
 * 正确写法： 通过接口名称，直接调用其中的静态方法
 * 格式：
 * 接口名称.静态方法名(参数);
 */

 public class demo03interface {

    public static void main(String[] args) {
        // 创建了实现类对象
        MyInterfaceStatic.methodStatic();
    }
 }