package javacode.introduction;
import java.util.Scanner;

public class person_introduction {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);


        System.out.println("enter your name");
        String name = scanner.nextLine();

        System.out.println("your name is " + name);

        scanner.close();



    }

}
