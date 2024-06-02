package InputOutput;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ExampleReadlineMethod {
    /* Method readline() can read all word in that line not character like method read() */
    public static void main(String[] args) {
        try{
            System.out.println("Enter character: ");
            InputStreamReader inReader = new InputStreamReader(System.in);
            BufferedReader buffer = new BufferedReader(inReader);

            String line  = buffer.readLine();
            System.out.println("You enter: " + line);
        }catch (IOException e){
            System.err.println("Error reading from user.");
        }
    }
}
