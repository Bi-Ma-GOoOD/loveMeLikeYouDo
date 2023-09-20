package Exception;

public class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);
        System.out.println(account);

        account.deposit(500);
        System.out.println(account);

        try{
            account.withdraw(15000);
            System.out.println(account);
        }catch (NotEnoughMoneyException e){
            System.err.println("Error" + " From:" + e.toString());
//            e.printStackTrace();
        }
    }
}
