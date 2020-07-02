public class MyInterfaceDefaultB implements MyInterfaceDefault {

    @Override
    public void methodAbs() {
        System.out.println("接口的实现类， BBBB");
    }

    @Override
    public void methodDefault() {
        System.out.println("接口的实现类， 实现默认方法的重写");
    }
}