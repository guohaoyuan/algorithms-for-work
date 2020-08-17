package 内部类;

public class demo02InnerClass {

    int num = 10;   // 外部类的成员变量

    public class Inner {

        int num = 20;   // 内部类成员变量

        public void methodInner() {
            int num = 30;   // 内部类方法的局部变量
            System.out.println(num);    // 局部变量，就近原则
            System.out.println(this.num);   // 内部类的成员变量
            System.out.println(demo02InnerClass.this.num);  // 外部类的成员变量
        }
    }
}
