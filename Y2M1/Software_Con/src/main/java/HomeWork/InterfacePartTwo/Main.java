/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.InterfacePartTwo;

import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        Product[] products = {new Product("Omo",50), new Product("Sugar",109), new Product("Candy",10)};
        System.out.println("^.^ Sort Price ^.^ ");

        Comparator<Product> productNameComparator = Comparator.comparing(Product::getName);

        Data.sort(products, productNameComparator);
        for (Product product : products) {
            System.out.println(product.getName() + ": " + product.getPrice());
        }

        Car[] cars = {new Car("Bulgati",200),new Car("Ferrari",199),new Car("Rolet",199.5)};
        System.out.println("- - - - - - - - - -");
        System.out.println("^.^ Sort Kilo - driven ^.^ ");

        Comparator<Car> carLicenseComparator = Comparator.comparing(Car::getLicense);

        Data.sort(cars, carLicenseComparator);
        for (Car car : cars) {
            System.out.println(car.getLicense() + ": " + car.getKiloDriven());
        }
    }
}