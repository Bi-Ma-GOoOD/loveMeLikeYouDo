/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.Composition3;

import java.util.ArrayList;

public class Mailbox {
    private String user;
    private ArrayList<Email> emails;

    public Mailbox(String user){
        this.user = user;
        emails = new ArrayList<>();
    }

    public String getUser(){
        return user;
    }

    public void message(Email e){
        emails.add(e);
    }

    public String messageList(){
        StringBuffer messages = new StringBuffer();
        for(Email m : emails){
            messages.append(m.toString() + "----------\n");
        }
        return messages.toString();
    }
}
