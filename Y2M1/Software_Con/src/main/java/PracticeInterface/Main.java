package PracticeInterface;

public class Main {
    public static void main(String[] args) {
        Pianist pianist = new Pianist(new Piano());
        pianist.playMusic();
        /* อันนี้ก็ Polymorphism ตรง pianist.playMusic()
        โด๊ดเดียวนะ แต่ทำงานได้หลากหลายเพราะ ขึ้นอยู่กับ obj */

        pianist.setKeyboard(new Organ());
        pianist.playMusic();
    }
}
