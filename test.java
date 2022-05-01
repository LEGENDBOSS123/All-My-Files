import java.util.Scanner;
public class HelloWorld
{
	public static void main(String[] args) {
                Scanner myObj = new Scanner(System.in); 
                System.out.println("Type a number:");
                int num = myObj.nextInt(); // Read user input 
                String isPrime = "IS PRIME";

                for (int i = 2;i<num;i++){
                        if (num%i == 0){
                            isPrime = "IS NOT PRIME";
                        }
                }
                System.out.println("YOUR NUMBER "+isPrime);
	}
}
