package PracticeInterface;

public class ConversionMain {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(100);
//        Measurable[] meas = account;
//        double balanceAvg = Data.average(meas);
//        System.out.println("Average Balance " + balanceAvg);
        account.deposit(200);
        account.getBalance();
        account.getMeasure();

        Country country = new Country("Thailand", 50);

        // static type --- type ทางซ้ายมือของการประกาศตัวแปร ref
        //      static type จะไม่เปลี่ยนไปตลอดการทำงานของโปรแกรม
        // dynamic type --- type ของ object ที่ตัวแปร ref กำลังใช้งานอยู่
        //      dynamic type จะเปลี่ยนไปตาม object ที่ ref กำลังใช้งานอยู่
        Measurable meas = account; // --- dynamic type เป็น BankAccount แต่!!! meas สามารถเรียกใช้ Method จาก Measuable เท่านั้น
        meas.getMeasure(); // ---> ใช้เวอร์ชั่นของ BankAccount คืนต่าเป็น balance

        meas = country; // --- dynamic type เป็น country
        // ทำแบบนี้ได้ meas = new Country("UK", 65);
        meas.getMeasure(); // ---> ใช้เวอร์ชั่นของ Country คืนค่าเป็น area
    }
}
