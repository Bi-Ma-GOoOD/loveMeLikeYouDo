/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.Composition3;

import java.util.ArrayList;


public class ProcessEmail {
    private ArrayList<Mailbox> mailboxes;

    public ProcessEmail(){
        mailboxes = new ArrayList<Mailbox>();
    }

    public void send(Email e){
        Mailbox mail = findUser(e.getReader());
        mail.message(e);
    }

    public String readMessage(String user){
        Mailbox mail = findUser(user);
        return mail.messageList();
    }

    private Mailbox findUser(String user){
        for(Mailbox box : mailboxes){
            if(box.getUser().equals(user)){
                return box;
            }
        }
        Mailbox b = new Mailbox(user);
        mailboxes.add(b);
        return b;
    }
}
