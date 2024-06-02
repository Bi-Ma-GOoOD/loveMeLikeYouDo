package InputOutput;

import java.io.*;

public class UsePrintWriterToWriteFile {
    public static void main(String[] args) {
        FileWriter fileWriter = null;

        InputStreamReader inReader = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(inReader);

        try {
            fileWriter = new FileWriter("data/from-input-user.txt");
            PrintWriter out = new PrintWriter(fileWriter);

            System.out.println("Input text to file: ");
            String line = buffer.readLine();

            while(!line.equals(" ") && ((line = buffer.readLine()) != null)){
                out.println(line);
            }
            out.flush();

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
