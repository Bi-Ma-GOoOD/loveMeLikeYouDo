package PracticeInterface;

import javafx.scene.shape.Rectangle;

public class Data {
    public static double average(Measurable[] objects){
        double sum = 0;

        for(Measurable obj : objects){
            sum = sum + obj.getMeasure();
            /* ตรง obj.getMeasure อะ อันนี้แหละคือ หลักการของ Polymorphism
             เพราะว่า โค๊ดอยู่โค๊ดเดียว แต่ทำงานแตกต่างกัน ซึ่งเหตุผลที่ทำงานต่างกันเพราะว่า
              obj ที่เรารับว่า เรารับ BankAccount || Country */
        }

        if(objects.length > 0) return sum / objects.length;
        return 0;
    }

    public static double average(Object[] objects, Measurer meas){
        double sum = 0;

        for(Object object : objects){
            sum = sum + meas.measure(object); // polymorphism
        }

        if(objects.length > 0) return sum / objects.length;
        return 0;
    }

    public static Measurable larger(Measurable obj1, Measurable obj2 ){
        if(obj1.getMeasure() > obj2.getMeasure())
            return obj1;
        else
            return obj2;
    }
}
