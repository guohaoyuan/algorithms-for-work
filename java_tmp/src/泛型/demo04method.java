package 泛型;

/**
 * 格式 权限修饰符 <泛型> 返回值类型 方法名（参数列表（使用泛型）） {
 *     方法体
 * }
 */

public class demo04method {

    public <T> void method(T t) {
        System.out.println(t);
    }
}
