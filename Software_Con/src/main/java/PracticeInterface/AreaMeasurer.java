package PracticeInterface;


import javafx.scene.shape.Rectangle;

public class AreaMeasurer implements Measurer {
    @Override
    public double measure(Object object) {
        Rectangle rectangle = (Rectangle) object;
        return rectangle.getWidth() * rectangle.getHeight();
    }
}
