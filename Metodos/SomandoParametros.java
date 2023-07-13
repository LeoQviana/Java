package Metodos;

public class SomandoParametros {

	public static void main(String[] args) {
		SomarMetodos somar01 = new SomarMetodos();
		SomarMetodos somar02 = new SomarMetodos();
		
		System.out.println(somar01.somar(10,30));
		System.out.println(somar02.somar(10,30,30));

	}

}
