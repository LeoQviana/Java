package Fundamentos;

import java.util.Scanner;

public class Exercicio10 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("Digite um valor:");
		int num1 = entrada.nextInt();
	
		System.out.println("Digite um valor:");
		int num2 = entrada.nextInt();
		
		System.out.println("Digite um valor:");
		int num3 = entrada.nextInt();
		
		
		if (num1>num2 && num1>num3) {
			System.out.println("O primeiro numero é maior");}
		
		else if (num2>num1 && num2>num3)
			System.out.println(num2);
		
		else
			System.out.println(num3);

	}

}
