package InputOutput;

import java.io.*;

public class WriteFileBySerializable implements Serializable {
    private int width;
    private int height;

    public void setWidth(int width){
        this.width = width;
    }
    public void setHeight(int height){
        this.height = height;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public static void main(String[] args) {
        WriteFileBySerializable box = new WriteFileBySerializable();
        box.setWidth(50);
        box.setWidth(20);


        try {
            FileOutputStream fs = new FileOutputStream("data/space.ser");
            ObjectOutputStream os = new ObjectOutputStream(fs);

            os.writeObject(box);
            os.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
