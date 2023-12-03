/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.DesignPatternStore;

// นับว่าสินค้าในร้านมีสินค้าประเภทนี้อะ กี่อัน เช่น หนังสือที่ชื่อนี้มีกี่เล่ม
public class CountAllProduct implements Counter{
    @Override
    public int productCounter(Product product) {
        return 1;
    }
}
