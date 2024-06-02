package InputOutput;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class ReadFileByDeserializable {
    public static void main(String[] args) {
        try{
            FileInputStream fileSteam = new FileInputStream("data/space.ser");
            ObjectInputStream os = new ObjectInputStream(fileSteam);

            Object one = os.readObject();

            WriteFileBySerializable elf = (WriteFileBySerializable) one;

            System.out.println(elf);

            os.close();
        } catch (IOException e){
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}
