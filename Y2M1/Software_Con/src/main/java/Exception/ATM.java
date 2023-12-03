package Exception;

public class ATM {
    private BankAccount currentAccount;

    public void doTransaction(String type, double amount) throws NotEnoughMoneyException{
        currentAccount.withdraw(amount);
    }
}
