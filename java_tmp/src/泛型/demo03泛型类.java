package 泛型;

/**
 *
 * @param <T>
 */
public class demo03泛型类<T> {

    private T name;

    public void setName(T name) {
        this.name = name;
    }

    public T getName() {
        return name;
    }
}
