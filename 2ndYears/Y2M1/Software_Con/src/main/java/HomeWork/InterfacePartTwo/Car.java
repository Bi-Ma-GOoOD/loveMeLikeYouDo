/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.InterfacePartTwo;

public class Car{
    private String license;
    private double kiloDriven; // ระยะทางการขับ
    public String getLicense() {
        return license;
    }
    public double getKiloDriven() {
        return kiloDriven;
    }
    public Car(String license, double kiloDriven) {
        this.license = license;
        this.kiloDriven = kiloDriven;
    }
}