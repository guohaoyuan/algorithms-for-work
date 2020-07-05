import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

/**
 * linkedhashset继承hashset
 *      底层是哈希表（数组+链表/红黑树）+ 链表;多了一个链表保证元素的有序
 *      但也不允许重复
 */

 public class demo01 {

    public static void main(String[] args) {

        show02();
    }

    public static void show02() {

        Map<String, Integer> map = new HashMap<>();
        map.put("杨宇小宝贝", 18);
        int age = map.get("杨宇小宝贝");    // 自动拆箱
        System.out.println(age);
        System.out.println(map);
    }
 }