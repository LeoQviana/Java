package Fundamentos;

import java.util.Scanner;

public class While5 {

	public static void main(String[] args) {
		Scanner alunos = new Scanner(System.in);
		int totalAlunos;
		double somaNotas = 0;
		int contador = 0;
		System.out.println("Quantos alunos tem na sala?");
		totalAlunos = alunos.nextInt();
		while(contador<totalAlunos) {
			System.out.print("Digite a nota do aluno:" + (contador + 1) );
			double nota = alunos.nextDouble();
			somaNotas+=nota;
			contador++;
		}
		double media = somaNotas/totalAlunos;
		System.out.println("A media da turma e: " + media);
		alunos.close();
			
	}

}
