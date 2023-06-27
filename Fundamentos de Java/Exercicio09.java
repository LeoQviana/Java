package Fundamentos;

import java.util.Scanner;

public class Exercicio09 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner (System.in);
		System.out.println("Digite um valor:");
		int resp = entrada.nextInt();
		System.out.println(resp > 0 ? "Positivo" : resp < 0 ? "Negativo" : "Neutro");

}
}
