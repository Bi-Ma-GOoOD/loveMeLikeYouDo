package atm;

public class BankAccount {
    private double balance;

    public  BankAccount(){
        this(0);
    }

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount){
        if(amount <= 0)
            throw new IllegalArgumentException("Amount must be positive");
        this.balance += amount;
    }

    public void withdraw(double amount){
        if(amount <= 0)
            throw new IllegalArgumentException("Amount must be positive");
        if(amount > balance)
            throw new IllegalArgumentException("Amount must be less than balance");
        this.balance -= amount;
    }

    public double getBalance() {
        return balance;
    }
}
