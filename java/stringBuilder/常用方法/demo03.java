/**
 * string 和stringBuilder的相互转换
 * 
 * string -> stringBuilder:
 *              StringBuilder stb = new StringBuilder("abc");
 * 
 * stringBuilder -> string:
 *              .toString()
 */
public class demo03 {

    public static void main (String[] args) {
        StringBuilder stb = new StringBuilder("abc");
        System.out.println(stb.toString());
    }
}