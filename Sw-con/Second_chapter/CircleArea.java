package Second_chapter;
import java.util.Scanner;

public class CircleArea {
    public static void main(String[] args){
        Scanner key = new Scanner(System.in);

        System.out.print("Enter the radius: ");
        double radius = key.nextDouble();

        if(radius < 0) System.out.println("Error radius must be >= 0!!!");
        else{
            double area = 3.141*radius*radius;
            System.out.println("The area is " + area);
        }
    }
}
