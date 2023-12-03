/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.Composition2;

public class DetailSlip {
    private Product product;
    private int quantity;

    public DetailSlip(Product product, int quantity){
        this.product = product;
        this.quantity = quantity;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public double getSubtotal() {
        return product.getPrice() * quantity;
    }

    @Override
    public String toString(){
        return product.toString() + "       " + quantity + "        " + getSubtotal();
    }

}
