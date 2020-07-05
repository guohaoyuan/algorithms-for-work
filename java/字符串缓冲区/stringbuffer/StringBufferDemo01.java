// package java.字符串缓冲区.stringbuffer;
    /**
     * append将任意类型的数据添加到缓冲区，返回值一就是this
     * 
     * delete删除缓冲区的字符[start, end)，返回值this
     * 
     * insert在指定位置插入字符
     * 
     * replace在指定位置替换成新字符串
     * 
     * reverse将缓冲区的字符串逆序排列
     * 
     * toString() 继承object, 重写toString(), 将可变对象转换成不可变对象
     * 
     * 
     */
public class StringBufferDemo01 {

    public static void function() {
        StringBuffer buffer = new StringBuffer();

        // 调用append方法
        buffer.append(6);
        System.out.println(buffer);

        buffer.append("asdasdasd");

        // 调用delete方法, 含头不含尾 
        buffer.delete(0, 2);
        System.out.println(buffer);

        // 调用insert方法，插入字符串
        buffer.insert(3, 123456);
        System.out.println(buffer);

        // 调用replace方法
        buffer.replace(0, 3, "Q");
        System.out.println(buffer);

        // 调用reverse方法
        buffer.reverse();
        System.out.println(buffer);
    }

    public static void main(String[] args) {

        function();
    }

}