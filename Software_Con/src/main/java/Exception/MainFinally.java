package Exception;

public class MainFinally {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);

        try{
            account.withdraw(50);
            System.out.println("Withdraw successful");
        }catch(NotEnoughMoneyException e){
            System.out.println("Error: " + e.getMessage());
        }
        /*finally จะทำงานเสมอ ไม่ว่าจะมี Exception หรือ ไม่มี*/
        finally{
            System.out.println("YO!");
        }
    }
}
