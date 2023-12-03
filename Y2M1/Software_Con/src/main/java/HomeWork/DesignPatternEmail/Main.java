package HomeWork.DesignPatternEmail;


public class Main {
    public static void main(String[] args) {
        Email email1 = new Email("Pyke", "Seraphine", "Halalalalala");
        Email email2 = new Email("Veigo", "Akali", "The mist!!!");

        EmailSystem emailSystemCea = new EmailSystem(new SendCeasarSystem(2));
        EmailSystem emailSystemCi = new EmailSystem(new SendSwitchCipherSystem());

        emailSystemCea.createBox(email1.getRecipient());
        emailSystemCi.createBox(email2.getRecipient());

        emailSystemCea.send(email1);
        System.out.println(email1.getText());
        emailSystemCi.send(email2);
        System.out.println(email2.getText());
    }
}
