import java.util.Scanner;

public class main {

    public static void main(String[] args){
        Scanner reader = new Scanner(System.in);
        System.out.println("Please enter value for k:");
        float k = reader.nextFloat();
        System.out.println("Please enter value for m:");
        float m = reader.nextFloat();
        System.out.println("Please enter value for n:");
        float n =  reader.nextFloat();

        mendel_probability calc = new mendel_probability(k,m,n);
        double answer = calc.dominant_prob_calc();
        System.out.println("Answer ="+answer);
    }
}
