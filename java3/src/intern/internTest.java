package intern;

public class internTest {

    public static void main(String[] args) {
//        String s2 = "aa";
//        String s1 = new String("a") + new String("a");
//        String s3 = s1.intern();
//        System.out.println(s1 == s2);
//        System.out.println(s3 == s2);
//        System.out.println(s3 == s1);
        /**
         * false
         * true
         * false
         */
        String s1 = new String("a") + new String("a");
        String s3 = s1.intern();
        String s2 = "aa";
        System.out.println(s1 == s2);
        System.out.println(s3 == s2);
        System.out.println(s3 == s1);
        /**
         * true
         * true
         * true
         */

    }
}
