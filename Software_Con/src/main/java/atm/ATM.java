package atm;

public class ATM {
    //composition
    private Bank bank;
    private Customer loginCustomer;

    public ATM(Bank bank){
        this.bank = bank;
        this.loginCustomer = null;
    }

    public boolean validateCustomer(int id, int pin){
        // delegation คือ การมอบหมายงานให้ Obj อื่นช่วยทำงานแทนให้
        loginCustomer = bank.validataCustomer(id, pin);
        /*if(customer != =null) return true;
        * return false แต่ย่อได้กลายเป็นโค๊ดอันล่างอะ*/
        return loginCustomer != null;
    }

    public void deposit(double amount){
        // delegation
        loginCustomer.getAccount().deposit(amount);
    }

    public void withDraw(double amount){
        loginCustomer.getAccount().withdraw(amount);
    }

    public double getBalance(){
        return loginCustomer.getAccount().getBalance();
    }

    public void transfer(int idDestination, double amount){
        BankAccount from = loginCustomer.getAccount();
        if(bank.findCustomer(idDestination) != null){
            BankAccount to = bank.findCustomer(idDestination).getAccount();

            from.withdraw(amount);
            to.deposit(amount);
        }
    }

    public void end(){
        // การ logout
        loginCustomer = null;
    }

}
