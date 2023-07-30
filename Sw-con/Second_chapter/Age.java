package Second_chapter;

import java.util.Scanner;

public class Age {
    public static void main(String[] args){
        final int MINOR = 21;
        int age;
         Scanner key = new Scanner(System.in);
         System.out.print("Enter your age: ");
         age = key.nextInt();

        System.out.println("You entered: " + age);
        if(age < MINOR)
            System.out.println("You are still young. Enjoy.");
        System.out.println("You are experienced.");


    }
}
