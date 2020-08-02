package 泛型;

import java.util.ArrayList;
import java.util.Iterator;

public class demo02使用泛型 {

    /**
     * 好处：安全检测，将运行期（代码运行之后抛出的异常）异常，提前到编译期（写代码时报错）
     */
    public static void main(String[] args) {

        ArrayList<String> array = new ArrayList<>();
        array.add("abc");
//        array.add(1);

        Iterator<String> it = array.iterator();
        while (it.hasNext()) {
            String s = it.next();
            System.out.println("字符串长度：" + s.length());
        }
    }
}
