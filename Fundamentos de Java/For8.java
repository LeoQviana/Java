package Fundamentos;

public class For8 {

	public static void main(String[] args) {
		int multiplo3 = 0, multiplos5 = 0;
		for (int i =1; i<=20;i++) {
			if(i%3==0){
				multiplo3 = multiplo3+i;
			}if(i%5==0){
				multiplos5 = multiplos5+i;
			}
	
	}System.out.println("A soma dos multiplos de 3:"+multiplo3);

		System.out.println("A soma dos multiplos de 5:" +multiplos5);
	int soma = multiplo3+multiplos5;
	System.out.println("A soma dos multiplos de 3 e 5 :"+ soma);
}

}


