package Fundamentos;

import java.util.Scanner;

public class Exercicio08 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("Digite um valor");
		int resp = entrada.nextInt();
		System.out.println(resp);
		if (resp>0)  
			System.out.println("Positivo");
		if (resp == 0)
			System.out.println("Neutro");
		else 
			System.out.println("Negativo");
		}
		
	}


