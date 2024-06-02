package atm;

public class Customer {
    //attribute
    private int id;
    private String name;
    private int pin;
    //composition
    private BankAccount account;

    // refactor : improve program design โดยที่ฟังกชันการทำงานไม่เปลี่ยน
    public Customer(int id, String name, int pin) {
        this(id, name, pin, 0);
//        this.id = id;
//        this.name = name;
//        this.pin = pin;
//        this.account = new BankAccount();
    }
    public Customer(int id, String name, int pin, double balance) {
        this.id = id;
        this.name = name;
        this.pin = pin;
        this.account = new BankAccount(balance);
    }

    public boolean checkPin(int pin){
        return this.pin == pin;
    }

    public void setPin(int currentPin, int newPin, int confirmPin){
        if(this.pin != currentPin) return;
        if(newPin == confirmPin) this.pin = newPin;
    }

    public int getId() {
        return id;
    }
    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public BankAccount getAccount() {
        return account;
    }

}
