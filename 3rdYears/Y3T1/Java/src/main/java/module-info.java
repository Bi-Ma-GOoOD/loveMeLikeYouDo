module home.personal.java {
    requires javafx.controls;
    requires javafx.fxml;


    opens home.personal.java to javafx.fxml;
    exports home.personal.java;
}