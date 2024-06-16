package Homework2;

//Himanshu Rana 
//"I pledge my honor that I abided by the Stevens Honor System" 

public class Complexity {
	
	
	//n^2
	public void method1 (int n) {
		int counter = 0; 
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				System.out.println("Operation" + counter); 
				counter++; 
			}
		}
	}
	
	//n^3
	public void method2 (int n) {
		int counter = 0; 
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				for(int k = 0; k < n; k++) {
					System.out.println("Operation" + counter); 
					counter++;
				}
				 
			}
		}
		
	}


	//log n
	public void method3 (int n) {
		int counter = 0; 
		for(int i = 1; i < n; i*=2) {
			System.out.println("Operation" + counter); 
			counter++;
		}
	
	}

	//n log n
	public void method4 (int n) {
		int counter = 0; 
		for(int i = 0; i < n; i++) {
			for(int j = 1; j < n; j*=2) {
				System.out.println("Operation" + counter); 
				counter++;
			}
		}
	
	}

	//log log n
	public void method5 (int n) {
		int counter = 1; 
		for (int i = n; i > 2; i = (int) Math.sqrt(i)) {
			System.out.println("Operation" + counter); 
			counter++;
		}
			
	}

	
	
	//optional - 2^n
	public int method6 (int n) {
		int counter = 1; 
		if (n <= 1) {
			counter++; 
			return n; 
		}
		else {
			counter++; 
			return method6(n - 2) + method6(n - 1); 
			
		}
		
		
		
	}
	
	
	public static void main(String args []) {
		Complexity c1 = new Complexity(); 
		c1.method5(8);
	}

}
