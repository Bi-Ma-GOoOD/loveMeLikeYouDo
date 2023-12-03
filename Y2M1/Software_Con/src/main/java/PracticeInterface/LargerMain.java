package PracticeInterface;

public class LargerMain {
    public static void main(String[] args) {
        Country uraguay = new Country("Uraguay", 176220);
        Country thailand = new Country("Thailand", 514000);

        Measurable max = Data.larger(uraguay,thailand);

//        String countryName = max.getName();
//          แบบนี้ทำไม่ได้นะคับ เพราะว่า Static type เป็น Measurable ซึ่งไม่มี Method getName ก็ใช้งานไม่ได้
        // วิธีแก้
//        Country maxCountry;
//        if(max instanceof Country)
//            maxCountry = (Country) max;
        Country maxCountry = (Country)max;
        String name = maxCountry.getName();
        System.out.println(name);
    }
}
