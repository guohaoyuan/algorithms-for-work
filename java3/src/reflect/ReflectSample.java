package reflect;

import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class ReflectSample {

    public static void main(String[] args) throws ClassNotFoundException, IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException, NoSuchFieldException {
        Class rc = Class.forName("reflect.Robot");
        Robot r = (Robot) rc.newInstance();
        System.out.println("Class name is:" + rc.getName());

        // 反射private方法
        Method getHello = rc.getDeclaredMethod("throwHello", String.class);
        getHello.setAccessible(true);   // 为了调用私有方法
        Object str = getHello.invoke(r, "Bob"); // 为了传参
        System.out.println("getHello result is " + str);

        // 反射public方法
        Method sayHi = rc.getMethod("sayHi", String.class);
        sayHi.invoke(r, "Welcome");

        // 反射private属性
        Field name = rc.getDeclaredField("name");
        name.setAccessible(true);
        name.set(r, "Alice");

        // 调用方法
        sayHi.invoke(r, "Welcome");
    }
}
