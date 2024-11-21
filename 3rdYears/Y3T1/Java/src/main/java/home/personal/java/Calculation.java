package home.personal.java;

public class Calculation {
    public static void main(String[] args) {
        forLoop(17);
        forEachLoop();
        whileLoop(20);
        breakForce(10, 8);
        iSayContinue(5, 4);
    }
    public static void forLoop(int x){
        System.out.println("\n[From : sum Function.]");
        int sum = 0;
        for(int i = 1; i <= x; i++){
            sum += i;
        }
        System.out.println("Sum of " + x + " is " + sum);
    }
    public static void forEachLoop(){
        System.out.println("\n[From : forEachLoop Function.]");
        System.out.println("I'm practicing :");
        String[] language = {"Python", "Java", "C"};
        for(String get_lang : language){
            System.out.println(get_lang);
        }
    }
    public static void whileLoop(int x){
        System.out.println("\n[From : whileLoop Function.]");
        int i = 0;
        System.out.println("Print the first even number of " + x);
        while(i <= x){
            System.out.println(i);
            i+=2;
        }
    }
    public static void breakForce(int x, int y){
        System.out.println("\n[From : breakForce Function.]");
        System.out.println("We must count from 0 - " + x);
        for(int i = 0; i < x; i++){
            System.out.println(i);
            if(i == y) break;
        }
        System.out.println("But we have limit count at " + y);
    }
    public static void iSayContinue(int x, int y){
        for(int i = 0; i <= 2; i++){
            for(int j = i; j<= x; j++){
                if(j == y) continue;
                System.out.println(j);
            }
        }
    }
}
