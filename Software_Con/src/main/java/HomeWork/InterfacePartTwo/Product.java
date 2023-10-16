/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.InterfacePartTwo;

public class Product{
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
}
