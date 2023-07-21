package Polimorfismo;

public class AnimalMain {
	public static void main(String[] args) {
		Animal animal = new Animal();
		animal.fazerBarulho();
		
		Cachorro cachorro = new Cachorro();
		cachorro.fazerBarulho();
		
		cachorro.fazerBarulho(3);
		cachorro.fazerBarulho("Au au");
		
	}
}