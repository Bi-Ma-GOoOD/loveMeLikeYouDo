package atm;

import java.util.HashMap;
import java.util.Map;

public class DataSourceDB {
    public Map<Integer, Customer> readCustomers() {
        // simulate read form database
        Map<Integer, Customer> customerMap = new HashMap<>();

        customerMap.put(1, new Customer(1, "Pyke", 1234, 1000));
        customerMap.put(2, new Customer(2, "Seraphine", 1234, 1000));
        customerMap.put(3, new Customer(3, "Viego", 1234, 1000));

        return customerMap;
    }
}
