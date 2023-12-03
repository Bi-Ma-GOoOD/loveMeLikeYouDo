/* นาย อัครพล พลายใย 6510451115 */

package HomeWork.Composition2;

import java.util.ArrayList;
import java.util.List;

public class SlipStructure {
    private List<DetailSlip> products;

    public SlipStructure(){
        this.products = new ArrayList<>();
    }

    public void purchase(Product product, int quantity){
        products.add(new DetailSlip(product, quantity));
    }

    public double getTotal(){
        double total = 0;
        for(DetailSlip s : products){
            total += s.getSubtotal();
        }
        return total;
    }

    @Override
    public String toString(){
        String content = "---------- INVOICE ----------\n";
        content += "Description     Price       Qty     Subtotal\n";

        for(DetailSlip s : products){
            content += " " + s.toString() + "\n";
        }
        content += "\nTOTAL TO PAY: " + getTotal();
        return content;
    }
}
