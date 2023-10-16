package atm;

import java.util.Map;

public class Bank {
    // attribute
    private String name;

    // composition
    private Map<Integer, Customer> customers;
    private DataSourceDB dataSource;

    public Bank(String name) {
        this.name = name;
        this.dataSource = new DataSourceDB();
        this.customers = dataSource.readCustomers();
    }

    public void registerCustomer(Customer customer){
        customers.put(customer.getId(), customer);
    }
    public Customer validataCustomer(int id, int pin){
        Customer findCustomer = customers.get(id);
        if(findCustomer != null){
            if(findCustomer.checkPin(pin))
                return findCustomer;
        }
        return null;
    }

    Customer findCustomer(int id){
        return customers.get(id);
    }
}
