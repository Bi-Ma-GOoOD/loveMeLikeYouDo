package InputOutput;

import java.io.*;

public class ReadFromFile {
    public static void main(String[] args){
        String fileName = "data/from-input-user.txt";
        try {
            FileReader fileReader = new FileReader(fileName);
            BufferedReader buffer = new BufferedReader(fileReader);

            System.out.println("Open file [ " + fileName + " ]");
            String line = buffer.readLine();

            while(line != null){
                System.out.println(line);
                line = buffer.readLine();
            }
        } catch (FileNotFoundException e){
            System.err.println("Cannot open file " + fileName);
        } catch (IOException e){
            System.err.println("TT Error reading from file");
        }
    }
}