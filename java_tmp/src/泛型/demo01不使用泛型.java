package 泛型;

import java.util.ArrayList;
import java.util.Iterator;

public class demo01不使用泛型 {

    public static void main(String[] args) {
        // 不使用泛型，导致不安全
        ArrayList array = new ArrayList();

        array.add("abc");
        array.add(1);

        // 获取集合的迭代器
        Iterator it = array.iterator();
        // 利用hasNext和next方法遍历集合
        while (it.hasNext()) {
            Object obj = it.next();
            System.out.println("当前元素： " + obj);

            // length是字符串特有方法，需要向下转型，导致溢出
            String s = (String)obj;
            int l = s.length();
            System.out.println("长度： " + l);
        }
    }
}
