public class Increment {
    public static void main(String[] args){
        int x, y;
        x = 10;
        y = x++;
        System.out.println("x = " + x + " y = " + y);
        y = ++x;
        System.out.println("x = " +x+ " y = " + y);
    }
}
