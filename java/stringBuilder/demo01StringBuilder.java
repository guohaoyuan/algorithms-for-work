/**
 * stringbuilder 是字符串缓冲区，可以提高字符串的效率
 * 
 * 实现方法有两种：
 *  1. 建立空的stringBuilder
 *  2. 建立一个STringDuilder，并将字符串内容加进去
 */
public class demo01StringBuilder {

    public static void main(String[] args) {

        StringBuilder stb = new StringBuilder();
        System.out.println("stb:" + stb);

        StringBuilder stb2 = new StringBuilder("jia you");
        System.out.println("stb2:" + stb2);
    }
}