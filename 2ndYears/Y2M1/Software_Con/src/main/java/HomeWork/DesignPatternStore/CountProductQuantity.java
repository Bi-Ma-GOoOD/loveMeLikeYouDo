/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.DesignPatternStore;

// นับว่าจำนวนของสินค้าชนิดนั้นๆอะ ถ้าเรามารวมกันจะได้เท่าไร เช่น A(2) + B(3) = 5 ประมาณนี้
public class CountProductQuantity implements Counter{
    @Override
    public int productCounter(Product product) {
        return product.getQuantity();
    }
}
