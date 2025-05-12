package InputOutput;

import java.io.*;

public class UseBufferWriterToWriteFile {
    public static void main(String[] args) {
        FileWriter fileWriter = null;
        InputStreamReader inReader = new InputStreamReader(System.in);
        BufferedReader buffer = new BufferedReader(inReader);

        try {
            fileWriter = new FileWriter("data/input-user-102.txt");
            BufferedWriter out = new BufferedWriter(fileWriter);

            System.out.println("Input text file: ");
            String line = buffer.readLine();

            while((!line.equals("end"))){
                out.write(line);
                out.newLine();
                line = buffer.readLine();
            }
            out.flush();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
