package 内部类;

public class Body {

    public class Heart {

        // 内部类的方法
        public void beat() {
            System.out.println("心脏跳动：泵泵泵！");
            System.out.println("我叫：" + name);
        }
    }

    // 外部类的成员变量
    private String name;

    // 外部类的方法
    public void methodBody() {
        System.out.println("外部类的方法");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
