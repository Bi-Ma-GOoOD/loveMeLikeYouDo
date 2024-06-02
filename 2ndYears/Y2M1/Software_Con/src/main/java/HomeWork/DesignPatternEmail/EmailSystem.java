package HomeWork.DesignPatternEmail;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class EmailSystem {
    private HashMap<String, List<Email>> mailboxes;
    private SendSystem send;

    public EmailSystem(SendSystem sendEncrypt) {
        send = sendEncrypt;
        this.mailboxes = new HashMap<>();
    }
    public void send(Email mail) {
        String encrypted = send.sendSystem(mail.getText());
        mail.setText(encrypted);
        // deliver to corresponding mailbox
        List<Email> box = mailboxes.get(mail.getRecipient());
        mailboxes.put(mail.getRecipient(), box);
        box.add(mail);
    }

    public void createBox(String name){
        mailboxes.put(name,new ArrayList<>());
    }
}
