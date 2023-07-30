package Second_chapter;
import java.util.Scanner;

public class TestSumInt {
    public static void main(String[] args) {
        int num,sum = 0;

        Scanner key = new Scanner(System.in);
        for(int i = 1; i <= 5; i++){
            System.out.print("Input number " +i+ " : ");
            num = key.nextInt();
            sum += num;
        }
        System.out.println("Sum = " +sum);
    }
}
