package Second_chapter;
import java.util.Scanner;
public class SwitchDemo {
    public static void main(String[] args) {
        int number;

        Scanner key = new Scanner(System.in);
        System.out.print("Choose number 1 2 or 3 to enter: ");
        number = key.nextInt();

        switch (number){
            case 1:
                System.out.println("You Entered 1.");
                break;
            case 2:
                System.out.println("You Entered 2.");
                break;
            case 3:
                System.out.println("You Entered 3.");
                break;
            default:
                System.out.println("That's not 1, 2, or 3!");
        }
    }
}
