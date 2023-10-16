/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.DesignPatternStore;

public class Main {
    public static void main(String[] args) {
        Store store = new Store();

        store.addProduct("Big Java",300,5);
        store.addProduct("Da vinci Code",120,0);
        store.addProduct("Python 101",200,10);

        System.out.println("Stock have : " + store.countProduct(new CountAllProduct()) + " main products.");
        System.out.println("Current products amount in stock : " + store.countProduct(new CountProductInStock()) + " main products");
        System.out.println("In " + store.countProduct(new CountProductInStock()) + " main products they have " + store.countProduct(new CountProductQuantity())
                + " lists ");
    }
}
