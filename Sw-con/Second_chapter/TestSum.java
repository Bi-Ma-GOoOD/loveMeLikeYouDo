package Second_chapter;
import java.util.Scanner;
public class TestSum {
    public static void main(String[] args) {
        double sum = 0;
        double num;

        Scanner key = new Scanner(System.in);
        System.out.print("Enter your number: ");
        num = key.nextDouble();

        for(int i = 1; i <= num; i++)
            sum += i;
        System.out.println("Sum = " + sum);
    }
}
