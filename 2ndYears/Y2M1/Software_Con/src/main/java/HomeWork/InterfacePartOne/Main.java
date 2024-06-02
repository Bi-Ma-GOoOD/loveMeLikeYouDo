/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.InterfacePartOne;


public class Main {
    public static void main(String[] args) {

        Product[] products = {new Product("Omo",50), new Product("Sugar",109), new Product("Candy",10)};
        System.out.println("^.^ Sort Price  ^.^ ");

        Data.sort(products);
        for(Product producter : products){
            System.out.println(producter.getName());
        }

        Car[] cars = {new Car("Bulgati",200),new Car("Ferrari",199),new Car("Rolet",199.5)};

        System.out.println("- - - - - - - - - -");
        System.out.println("^.^ Sort Kilo - driven ^.^ ");

        Data.sort(cars);
        for(Car carer : cars){
            System.out.println(carer.getLicense());
        }


    }
}
