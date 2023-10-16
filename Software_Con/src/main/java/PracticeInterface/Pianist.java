package PracticeInterface;

//pianist is a keyboard --- ไม่ใช่ Is-A relationship
public class Pianist {
    //HAS-A relationship
    //pianist has keyboard
    //instance variable ที่เป็น object type
    private Keyboard keyboard;

    public Pianist(Keyboard keyboard){
        this.keyboard = keyboard;
    }
    public void setKeyboard(Keyboard keyboard){
        this.keyboard = keyboard;
    }
    public void playMusic(){
        keyboard.pressWhiteKey(1);
        keyboard.pressWhiteKey(2);
        keyboard.pressWhiteKey(3);
    }
}
