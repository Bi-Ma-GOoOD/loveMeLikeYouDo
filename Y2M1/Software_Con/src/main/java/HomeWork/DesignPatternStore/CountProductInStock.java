/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.DesignPatternStore;

// สมมติว่า มีหนังสือ สาม เล่ม class นี้ จะนับว่า จากทั้งหมด สาม ประเภท ตอนนี้เหลือเท่าไร
public class CountProductInStock implements Counter {
    @Override
    public int productCounter(Product product) {
        if (product.getQuantity() > 0) return 1;
        return 0;
    }
}
