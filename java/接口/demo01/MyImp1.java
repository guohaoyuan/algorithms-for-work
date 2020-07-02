public class MyImp1 implements MyInterfaceAbstract {
    @Override   // 重写
    public void methodAbs1() {
        System.out.println("第一个抽象方法");
    }

    @Override
    public void methodAbs2() {
        System.out.println("第二个抽象方法");
    }
}