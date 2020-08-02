package 装箱拆箱;

import java.util.ArrayList;
import java.util.Hashtable;

public class demo01 {

    public static void main(String[] args) {
        Integer i = 1;

        int j = i;

        Integer k = 1;

        // 缓存区，常量池
        // 比较地址
        System.out.println(i == k);
        // 比较内容
        System.out.println(i.equals(k));

        // 初试单例
        System.out.println(false == false);

        System.out.println("================");

        String s1 = "ghy";
        String s2 = "ghy";
        System.out.println(s1 == s2);

        String s3 = new String("ghy");
        String s4 = new String("ghy");
        System.out.println(s1 == s3);
        System.out.println(s3 == s4);
        System.out.println(s3.equals(s4));

        System.out.println("================");

        Integer num1 = Integer.valueOf(1);
        Integer num2 = Integer.valueOf(1);
        System.out.println(num1 == num2);

        ArrayList<Integer> a1 = new ArrayList<>();
        a1.add(1);
//        a1.removeIf();
    }
}
