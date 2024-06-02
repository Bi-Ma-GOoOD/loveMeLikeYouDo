package Exception;

/* การสร้าง Exception แบบนี้อะ จะเป็นการสร้าง Exception แบบ Checked Exception*/
public class NotEnoughMoneyException extends Exception{

    public NotEnoughMoneyException() {
    }
    public NotEnoughMoneyException(String errorMessage){
        super(errorMessage);
    }
}
