package 泛型;

public class demo03test {
    public static void main(String[] args) {
        demo03泛型类<Integer> demo1 = new demo03泛型类<>();
        demo1.setName(1);

        // 自动装箱
        Integer name = demo1.getName();
        System.out.println(name);

        demo03泛型类<String> demo2 = new demo03泛型类<>();
        demo2.setName("ghy");
        String name1 = demo2.getName();
        System.out.println(name1);

    }

}
