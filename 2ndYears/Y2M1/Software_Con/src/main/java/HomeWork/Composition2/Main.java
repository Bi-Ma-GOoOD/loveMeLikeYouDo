/* นาย อัครพล พลายใย 6510451115 */

package HomeWork.Composition2;

public class Main {
    public static void main(String[] args) {

        Product toaster = new Product("Toaster", 29.95);
        Product hairDryer = new Product("Hair dryer", 24.95);
        Product carVacuum = new Product("Car Vacuum", 19.99);

        SlipStructure poro = new SlipStructure();
        poro.purchase(toaster,3);
        poro.purchase(hairDryer,1);
        poro.purchase(carVacuum,2);

        System.out.println(poro.toString());
    }
}
