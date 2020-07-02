/**
 *  * 接口当中可以定义成员变量， 但是必须使用public static final 三个关键字进行修饰
 * 从效果上将， 起始就是接口的常量
 * 格式：
 * public static final 数据类型 常量名称 = 数值;
 *
 * 一旦使用final关键字进行修饰，说明不可变
 * 
 * 注意事项：
 * 1. 接口中的常量，可以省略public static final 注意： 
 * 2. 接口中的常量， 必须赋值
 * 3. 接口中常量使用大写字母，使用下划线进行分割
 */


 public interface MyInterfaceConst {

    // 这其实是一个常量
    public static final NUM = 10;
    // 调用方式接口名称.变量名称
}
 