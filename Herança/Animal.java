package Herança;

public class Animal {
	public String nome;
	public double peso;
	public String cor;
	public String tipo_pelo;

	public Animal(String _nome, double _peso, String _cor, String _tipo_pelo) {
		this.nome = _nome;
		this.peso = _peso;
		this.cor = _cor;
		this.tipo_pelo = _tipo_pelo;
		
}

	public void comer() {
		System.out.println(nome + "esta comendo.");
	}
	public void som() {
		System.out.println(nome + "esta fazendo barulho");
	}
}