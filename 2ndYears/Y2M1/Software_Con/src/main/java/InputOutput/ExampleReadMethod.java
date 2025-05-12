package InputOutput;

import java.io.IOException;

public class ExampleReadMethod {
    /* method read() can read only one character */
    public static void main(String[] args) {
        System.out.println("Enter characters: ");
        try {
            int inchar = System.in.read();
            char a = (char) inchar;
            System.out.println("You entered: " + a);
        } catch (IOException e) {
            System.err.println("Error reading from user");
        }
    }
}
