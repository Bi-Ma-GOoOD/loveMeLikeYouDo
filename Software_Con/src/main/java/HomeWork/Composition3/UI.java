/* นาย อัครพล พลายใย 6510451115 */
package HomeWork.Composition3;

import java.util.Scanner;

public class UI {
    private Scanner in;

    /* UI. */
    public UI() {
        in = new Scanner(System.in);
    }

    /* e-mail messaging system */
    public void run(ProcessEmail system) {

        boolean more = true;
        String currentUser = null;

        System.out.println("=========== SWCon Email System ===========");

        while (more) {
            System.out.println(
                    "Command --> Log I)n  S)end message  R)ead messages  Log O)ut  Q)uit");
            String command = in.nextLine().toUpperCase();

            if (command.equals("I")) {
                System.out.println("HI Nice to see you again!!!");
                System.out.print("User name: ");
                currentUser = in.nextLine();
            }
            else if (command.equals("O")) {
                System.out.println("GOOD BYE ~~~~");
                currentUser = null;
            }
            else if (command.equals("Q")) {
                System.out.println("See Yahhh next time ~~~");
                more = false;
            }
            else if (command.equals("R")) {
                if (currentUser == null) {
                    System.out.println("Log in first!");
                } else {
                    System.out.println("- - - Reading Mode - - -");
                    System.out.println(system.readMessage(currentUser));
                }
            }
            else if (command.equals("S")) {
                if (currentUser == null) {
                    System.out.println("Log in first!");
                }
                else {
                    System.out.println("- - - Sending Mode - - -");
                    System.out.print("Enter recipient: ");
                    String to = in.nextLine();
                    System.out.print("Enter text: ");
                    String text = in.nextLine();
                    Email msg = new Email(currentUser, to, text);
                    system.send(msg);
                }
            }
        }
    }
}