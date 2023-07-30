package Second_chapter;

import java.util.Arrays;
import java.util.Scanner;

public class Division {
    public static void main(String[] args) {
        double number1, number2;
        double quotient;

        Scanner key = new Scanner(System.in);
        System.out.print("Enter your number: ");
        number1 = key.nextDouble();
        System.out.print("Enter another number: ");
        number2 = key.nextDouble();

        if(number2 == 0){
            System.out.println("Division by zero is not possible.");
            System.out.println("Please run the program again and ");
            System.out.println("enter a number other than zero.");
        }
        else{
            quotient = number1/number2;
            System.out.print("The quotient of " + number1);
            System.out.print(" divided by " + number2);
            System.out.println(" is " + quotient);
        }
    }
}
