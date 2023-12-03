module ku.cs.software_con {
    requires javafx.controls;
    requires javafx.fxml;


    opens ku.cs.software_con to javafx.fxml;
    exports ku.cs.software_con;
}