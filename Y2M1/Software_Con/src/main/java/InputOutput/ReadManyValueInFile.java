package InputOutput;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ReadManyValueInFile {
    public static void main(String[] args) {
        String fileName = "data/food.txt";
        List<Restaurant> restaurants = new ArrayList<Restaurant>();

        try {
            FileReader fileReader = new FileReader(fileName);
            BufferedReader buffer = new BufferedReader(fileReader);

            String line = null;

            while((line = buffer.readLine()) != null){
                String [] data = line.split(",");
                String name = data[0].trim();
                String type = data[1].trim();
                String area = data[2].trim();
                int rating = Integer.parseInt(data[3].trim());

                Restaurant r = new Restaurant(name, type, area);
                r.setRating(rating);
                restaurants.add(r);
                System.out.println(line);
            }
        } catch (FileNotFoundException e) {
            System.err.println("Cannot read file " + fileName);
        } catch (IOException e) {
            System.err.println("Error reading from file");
        }
    }
}
