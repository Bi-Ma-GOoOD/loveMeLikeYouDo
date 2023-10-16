package PracticeInterface;

public class MainForTestAverage {
    public static void main(String[] args) {
        BankAccount[] bankAccounts = {new BankAccount(100), new BankAccount(200)
            ,new BankAccount(300)};

        double balanceAvg = Data.average(bankAccounts);
        System.out.println("Average Balance " + balanceAvg);

        Country[] country = {new Country("Thailand",50), new Country("UK",69)
                ,new Country("Mexico",80)};

        double countryAvg = Data.average(country);
        System.out.println("Average Area = " + countryAvg);
    }
}
