package HomeWork.DesignPatternEmail;

public class SendSwitchCipherSystem implements SendSystem{
    SendSwitchCipherSystem() {}
    @Override
    public String sendSystem(String message) {
        char[] data = message.toCharArray();
        for (int i = 0; i < data.length-1; i += 2) {
            char tmp = data[i];
            data[i] = data[i+1];
            data[i+1] = tmp;
        }
        return new String(data);
    }
}
