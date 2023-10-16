package PracticeInterface;

public class Country implements Measurable,Comparable{
    private String name;
    private double area;
    private int population;
    private double gdp;

    public Country(String name, double area) {
        this.name = name;
        this.area = area;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setArea(double area) {
        this.area = area;
    }

    public void setPopulation(int population) {
        this.population = population;
    }

    public void setGdp(double gdp) {
        this.gdp = gdp;
    }

    public String getName() {
        return name;
    }

    public double getArea() {
        return area;
    }

    public int getPopulation() {
        return population;
    }

    public double getGdp() {
        return gdp;
    }

    @Override
    public String toString() {
        return "Country{" +
                "name='" + name + '\'' +
                ", area=" + area +
                ", population=" + population +
                ", gdp=" + gdp +
                '}';
    }

    public int compareTo(Object otherObject){
        Country other = (Country)otherObject;
        /* เรียงด้วยชื่อ */
        return this.name.compareTo(other.name);
        /* เรียงด้วยเลข*/
//        if(this.area < other.area) return -1;
////        if(this.area > other.area) return 1;
////        return 0;
    }
    /*การใส่ @Override จะใส่ไม่ใส่ก็ได้ แต่ถ้าใส่ก็ดีกว่า*/
    @Override
    public double getMeasure() {
        return 0;
    }

    @Override
    public double getMeasureForLeast() {
        return 0;
    }
}
