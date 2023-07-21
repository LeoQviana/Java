package Polimorfismo;

public class Animal {
	public void fazerBarulho() {
		System.out.println("O animal esta fazendo barulho!");
	}
	
	public void fazerBarulho(String som) {
		System.out.println("O animal esta fazendo o seguinte som: " + som);
	}
}
class Cachorro extends Animal {
	public void fazerBarulho() {
		System.out.println("O cachorro esta latindo.");
	}
	
	public void fazerBarulho(int intensidade) {
		String som = "au".repeat(intensidade);
		System.out.println("O cachorro esta latindo "+ intensidade + "vezes:" + som);
	}
		
	}