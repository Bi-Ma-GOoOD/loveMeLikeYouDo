import java.util.Scanner;

public class Total {
    public static void main(String[] args){
        int total;
        int x,y;

        Scanner key = new Scanner(System.in);

        System.out.print("Input x: ");
        x = key.nextInt();

        System.out.print("Input y: ");
        y = key.nextInt();
        total = x+y;
        System.out.println("The value is: " + total);
    }
}
