package PracticeInterface;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class CompareToMain {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount(300);
        BankAccount account2 = new BankAccount(500);

//        if(account1.compareTo(account2) < 0)
//            System.out.println("Account 1 < Account 2 ");
//        if(account1.compareTo(account2) > 0)
//            System.out.println("Account 1 > Account 2");
//        if(account1.compareTo(account2) == 0)
//            System.out.println("Account 1 = Account 2");


        ArrayList<BankAccount> arrayList = new ArrayList<>();
        arrayList.add(new BankAccount(100));
        arrayList.add(new BankAccount(10));
        arrayList.add(new BankAccount(1000));

        for(BankAccount account : arrayList)
            System.out.println(account);

        System.out.println("- - - - - -");

        Collections.sort(arrayList);
        for(BankAccount account : arrayList)
            System.out.println(account);

        Country[] countries = {new Country("TH", 50),
        new Country("UK", 60),
        new Country("Maxico", 55)};

        System.out.println("- - - - - -");

        for(Country country : countries)
            System.out.println(country);

        System.out.println("- - - - - -");

        Arrays.sort(countries);

        for(Country country : countries)
            System.out.println(country);
    }
}
