package InputOutput;

public class Restaurant {
    private String name;
    private String type;
    private String area;
    private int rating;
    public Restaurant(String name, String type, String area) {
        this.name = name;
        this.type = type;
        this.area = area;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public String getName() {
        return name;
    }

    public String getArea() {
        return area;
    }

    public String getType() {
        return type;
    }

    public int getRating() {
        return rating;
    }
}
