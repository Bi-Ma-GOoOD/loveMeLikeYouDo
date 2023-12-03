/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.Composition3;

public class Email {
    private String sender;
    private String reader;
    private String message;

    public Email(String sender, String reader, String message){
        this.message = message;
        this.reader = reader;
        this.sender = sender;
    }

    public Email(String sender, String reader){
        this(sender,reader,"");
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getSender() {
        return sender;
    }

    public String getReader() {
        return reader;
    }

    public String getMessage() {
        return message;
    }

    public String toString(){
        return "From : " + sender + "\n" + "To : " + reader + "\n" + message + "\n";
    }
}
