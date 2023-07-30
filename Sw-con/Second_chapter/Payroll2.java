package Second_chapter;
import java.util.Scanner;

public class Payroll2 {
    public static void main(String[] args) {
        final double RATE = 150;
        final double STD_HOUR = 40;
        double pay = 0.0;

        Scanner key = new Scanner(System.in);
        System.out.print("Enter the number of hours worked: ");
        int hours = key.nextInt();
        if(hours > STD_HOUR)
            pay = RATE * STD_HOUR + ((hours-STD_HOUR)*(RATE*1.5));
        else
            pay = RATE * STD_HOUR;
        System.out.println("Pay = " + pay);
    }
}
