package 泛型;

import java.util.ArrayList;

public class demo06通配符 {
    public static void main(String[] args) {
        // 不确定传入参数类型
        // 在创建对象是要确定，传入的类型
        ArrayList<String> array1 = new ArrayList<>();
        ArrayList<Integer> array2 = new ArrayList<>();

        array1.add("a");

        array2.add(1);

        demo06通配符.method(array1);
        demo06通配符.method(array2);
    }

    public static <T> void method(ArrayList<T> a) {
        for (int i = 0; i < a.size(); i++){
            System.out.println(a.get(i));
        }
    }
}
