package InputOutput;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ReadAndUseNumberFromFile {
    public static void main(String[] args){
        String fileName = "data/number.txt";
        try {
            FileReader fileReader = new FileReader(fileName);
            BufferedReader buffer = new BufferedReader(fileReader);

            int sum = 0;
            String line = buffer.readLine();

            while(line != null){
                int num = Integer.parseInt(line);
                sum += num;
                line = buffer.readLine();
            }
            System.out.println("Total is: " + sum);
        } catch (FileNotFoundException e) {
            System.err.println("Cannot read file " + fileName);
        } catch (IOException e) {
            System.err.println("Error reading from file ");
        }
    }
}
