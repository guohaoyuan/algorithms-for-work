package hasdcode_and_equals.no_hashcode_equals;

import java.util.HashSet;

public class hashtest {
    public static void main(String[] args) {
        HashSet<Person> set = new HashSet<>();

        set.add(new Person("GHY", 24));
        set.add(new Person("YY", 18));
        set.add(new Person("GHY", 18));
        set.add(new Person("YY", 18));
        System.out.println(set);
    }
}
