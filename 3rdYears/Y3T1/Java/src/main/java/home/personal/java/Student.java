package home.personal.java;

public class Student {
    public static void main(String[] args) {
        simpleIfStatement(10, 5);
        ifElseBlock(10, 5);
        nestIf();
        switchNaja(11);
    }
    public static void simpleIfStatement(int x, int y){
        System.out.println("[From : simpleIfStatement Function.]");
        if(x > y){
            System.out.println("x > y, because x = 10 and y = 5");
        }else{
            System.out.println("No, It's not impossible.");
        }
    }
    public static void ifElseBlock(int x, int y){
        System.out.println("\n[From : ifElseBlock Function.]");
        if(x < y){
            System.out.println("Say Yes x < y ^.^");
        }else{
            System.out.println("Say No x > y TT.");
        }
    }
    public static void nestIf(){
        System.out.println("\n[From : nestIf Function.]");
        String city = "Delhi, India";
        if(city.endsWith("India")){
            if(city.contains("Meerut")){
                System.out.println("You live in Meerut city.");
            } else if (city.contains("Noida")) {
                System.out.println("You live in Noida city");
            }else{
                System.out.println(city.split(",")[0]);
            }
        }else{
            System.out.println("You not live in India Naja.");
        }
    }
    public static void switchNaja(int x){
        System.out.println("\n[From : switchNaja Function.]");
        int check = x % 2;
        switch (check) {
            case 0 -> System.out.println(x + " is a even number.");
            case 1 -> System.out.println(x + " is an odd number.");
        }
    }

}
