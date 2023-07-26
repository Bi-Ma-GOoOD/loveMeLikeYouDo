public class StringMethod {
    public static void main(String[] args){
        String message = "Java is Great Fun!";
        // ทำให้เป็นตัวใหญ่
        String upper = message.toUpperCase();
        // ทำให้เป็นตัวเล็ก
        String lower = message.toLowerCase();
        // ให้ตัวแปร letter เก็บอักขระตัวที่ 3 จาก String โดยตัวแรกเริ่มนับจาก 0
        char letter = message.charAt(3);
        // ให้ตัวแปร length เก็บค่าความยาวของ String
        int length = message.length();
        System.out.printf("%s have %d characters || Upper case: %s || Lower case: %s -- And 3th position of Java is Great Fun! is %c",message, length, upper, lower, letter);
    }
}
