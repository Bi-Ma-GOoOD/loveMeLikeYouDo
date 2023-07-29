import java.util.Scanner;
public class Payroll {
    public static void main(String[] args){
        String name; //เก็บชื่อพนักงาน
        int hours; //ชั่วโมงการทำงาน
        double payRate; //จำนวนเงินต่อชั่วโมง
        double grossPay; //จำนวนเงินทั้งหมด

        Scanner key = new Scanner(System.in);
        System.out.print("What is your name? ");
        name = key.nextLine();

        System.out.print("How many hours did you work this week? ");
        hours = key.nextInt();

        System.out.print("What is your hourly pay rate? ");
        payRate = key.nextInt();
        grossPay = hours * payRate;

        System.out.println("hello " + name);
        System.out.println("This week you work " + hours + " hours.");
        System.out.print("So your gross pay is " + grossPay);
    }
}
