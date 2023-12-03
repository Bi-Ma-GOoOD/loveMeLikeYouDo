package PracticeInterface;
import Exception.NotEnoughMoneyException;

public class BankAccount implements Measurable, Comparable{
    private double balance;

    public BankAccount(double balance){
        this.balance = balance;
    }
    public void deposit(double amount){
        balance += amount;
    }
    public void withdraw(double amount) throws NotEnoughMoneyException {
//        System.out.println("Before throw Exception");
        if(amount <= 0)
            throw new IllegalArgumentException("amount must be positive.");
        if(balance < amount)
            throw new NotEnoughMoneyException("Cannot withdraw BrOoO.");
//        System.out.println("After throw Exception");
        balance -= amount;
    }
    public double getBalance() {
        return balance;
    }
    @Override
    public String toString() {
        return "BankAccount{ " + "Balance }: " + balance;
    }

    @Override
    public double getMeasure() {
        return balance;
    }

    @Override
    public double getMeasureForLeast() {
        return 0;
    }

    @Override
    public int compareTo(Object otherObject) {
        BankAccount otherAccount = (BankAccount) otherObject;
        if(this.balance < otherAccount.balance) return -1;
        if(this.balance > otherAccount.balance) return 1;
        return 0;
    }
}
