/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.DesignPatternStore;

import java.util.ArrayList;
import java.util.List;

public class Store {
    private List<Product> products;
    public Store() { products = new ArrayList<>(); }
    public void addProduct(String name, double price, int quantity) {
        products.add(new Product(name, price, quantity));
    }
    public int countProduct(Counter counter){
        int count = 0;
        for(Product prod : products){
            count += counter.productCounter(prod);
        }
        return count;
    }
}
