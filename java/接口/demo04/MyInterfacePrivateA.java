/**
 * 1. 普通私有方法， 解决多个默认方法之间重复代码问题
 * 格式：
 * private 返回类型 方法名称（参数列表）{
 *      方法体
 * }
 * 2. 静态私有方法， 解决多个静态方法之间重复代码问题
 * 格式：
 * private static 返回值类型 方法名称（参数列表）{
 *      方法体 
 * }
 */
public interface MyInterfacePrivateA {
    
    public static void methodDefault1() {
        System.out.println("静态方法1");
        methodStaticCommon();
    }

    public static void methodDefault2() {
        System.out.println("静态方法2");
        methodStaticCommon();
    }

    private static void methodStaticCommon() {
        System.out.println("AA");
        System.out.println("BB");
        System.out.println("CC");
    }
}


















