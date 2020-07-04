/**
 * stringBuilder的常用方法 append()
 *   添加任意类型的字符串形式，返回值就是this，也就是对象本身
 */

 public class demo02StringBulder {

    public static void main(String[] args) {
        StringBuilder stb = new StringBuilder();

        stb.append(10);
        stb.append("Ac");
        stb.append("中");
        stb.append(true);

        System.out.println(stb);

        // reverse方法
        stb.reverse();
        System.out.println(stb);
    }
 }