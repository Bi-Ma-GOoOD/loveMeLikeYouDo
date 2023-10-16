package PracticeInterface;

import javafx.scene.shape.Rectangle;

public class MainRectangle {

    public static void main(String[] args) {
        Rectangle rectangle1 = new Rectangle(10, 20);
        Rectangle rectangle2 = new Rectangle(30, 10);
        Rectangle rectangle3 = new Rectangle(20, 20);

        Rectangle[] rectangles = {rectangle1, rectangle2, rectangle3};

        AreaMeasurer areaMeasurer = new AreaMeasurer();
        double areaAvg = Data.average(rectangles, areaMeasurer);
        System.out.println(areaAvg);


        /*inner class / trivial class */
        class HeightMeasurer implements Measurer{

            @Override
            public double measure(Object object) {
                Rectangle rectangle = (Rectangle) object;
                return rectangle.getHeight();
            }
        }

        /* anonymous class */
//        double perimeterAvg = Data.average(rectangles, new Measurer() {
//            @Override
//            public double measure(Object object) {
//                Rectangle rectangle = (Rectangle) object;
//                return 2 * ((rectangle.getHeight()) + rectangle.getWidth());
//            }
//        });
    }
}
