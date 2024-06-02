/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.InterfacePartOne;

public class Product implements MeasurableForLeast,Comparable<Product> {
    private String name;
    private double price; // ราคา

    public String getName() {
        return name;
    }
    public double getPrice() {
        return price;
    }

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public double getMeasureForLeast() {
        return price;
    }

    @Override
    public int compareTo(Product other) {
        if(this.price < other.price) return -1;
        if(this.price > other.price) return 1;
        return 0;
    }
}
