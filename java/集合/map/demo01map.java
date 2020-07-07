import java.util.Map;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class demo01map {

    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("GHY", 180);
        map.put("YY", 168);

        System.out.println(map);

        // 将map集合中的key抽出来
        Set<String> set = map.keySet();

        // 转换成迭代器
        Iterator<String> it = set.iterator();
        
        while(it.hasNext()) {
            String key = it.next();
            Integer value = map.get(key);
            System.out.println(value);
        }
        
        for(String key : set) {
            Integer value = map.get(key);
            System.out.println(value);
        }
    }
}