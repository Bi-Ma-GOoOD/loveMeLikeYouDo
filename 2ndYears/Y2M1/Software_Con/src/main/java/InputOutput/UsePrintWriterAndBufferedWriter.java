package InputOutput;

import java.io.*;

public class UsePrintWriterAndBufferedWriter {
    public static void main(String[] args) {
        FileWriter fileWriter = null;
        InputStreamReader inReader = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(inReader);

        try {
            fileWriter = new FileWriter("data/input-user-103.txt", true);
            PrintWriter out = new PrintWriter(new BufferedWriter(fileWriter));

            System.out.println("Input text to file: ");
            String line = buffer.readLine();

            while(!line.equals("end")){
                out.println(line);
                line = buffer.readLine();
            }
            out.flush();
        } catch (IOException e) {
            System.err.println("Error reading from user");
        }
        finally {
            try {
                buffer.close();
            } catch (IOException e) {
                System.err.println("Error closing files");
            }
        }
    }
}
