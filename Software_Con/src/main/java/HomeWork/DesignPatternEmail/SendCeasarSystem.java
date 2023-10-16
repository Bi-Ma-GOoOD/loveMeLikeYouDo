package HomeWork.DesignPatternEmail;

public class SendCeasarSystem implements SendSystem{
    private int key;
    public SendCeasarSystem(int key){
        this.key = key;
    }
    @Override
    public String sendSystem(String message) {
        char[] data = message.toCharArray();
        for (int i = 0; i < data.length; i++) {
            data[i] = (char)(data[i] + key);
        }
        return new String(data);
    }
}
