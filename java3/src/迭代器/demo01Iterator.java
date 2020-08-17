package 迭代器;

import java.util.ArrayList;
import java.util.Iterator;

public class demo01Iterator {

    public static void main(String[] args) {
        // 创建集合对象
        ArrayList<String> arrayList = new ArrayList<>();

        arrayList.add("GHY");
        arrayList.add("YY");
        arrayList.add("GHY!");

        // 多态实现迭代器
        Iterator<String> iterator = arrayList.iterator();

        boolean b = iterator.hasNext(); // 判断有无下一个元素
        System.out.println(b);

        // next取出下一个元素
        String s = iterator.next();
        System.out.println(s);

        // 没有元素是会跑池noSuchElementException
//        while (iterator.hasNext()) {
//            String s1 = iterator.next();
//            System.out.println(s1);
//        }
        for(String s1: arrayList) {
            System.out.println(s1);
        }
    }
}
