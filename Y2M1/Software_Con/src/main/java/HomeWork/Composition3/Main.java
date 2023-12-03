/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.Composition3;

public class Main {
    public static void main(String[] args) {
        ProcessEmail start = new ProcessEmail();
        UI ui = new UI();
        ui.run(start);
    }
}
