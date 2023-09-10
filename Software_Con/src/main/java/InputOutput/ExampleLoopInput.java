package InputOutput;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ExampleLoopInput {
    public static void main(String[] args) {
        try{
            InputStreamReader inReader = new InputStreamReader(System.in);
            BufferedReader buffer = new BufferedReader(inReader);

            System.out.println("Enter lines: ");
            String line = buffer.readLine();

            while(!line.equals("bye")){
                System.out.println("you entered: " + line);
                line = buffer.readLine();
            }
        } catch (Exception e){
            System.err.println("Error reading from user");
        }
    }
}
