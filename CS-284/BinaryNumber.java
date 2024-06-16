package Homework1;



// Himanshu Rana CS284 A
// "I pledge my honor that I have abided by the Stevens Honor System"


public class BinaryNumber {
	
	//Data fields
	private int[] data; 
	private boolean overflow; 
	
	/**
	 * This is a constructor that creates an binary number with the given length 
	 * and it only consists of 0
	 * @param length
	 */
	BinaryNumber(int length) { 
		data = new int[length]; 
		for(int x = 0; x < length; x++) {
			data[x] = 0; 
		}
		
	}
	/**
	 * This is a constructor that creates a binary number given a string 
	 * @param str
	 */
	BinaryNumber(String str) {
		data = new int[str.length()];
		for(int x = 0; x < str.length(); x++) {
			char index = str.charAt(x); 
			data[x] = Character.getNumericValue(index); 
		}
		
				
		
	}
	
	/**
	 * This function gets the length of the binary number. 
	 * @return the length 
	 */
	public int getLength() {
		return data.length; 
		
	}
	/**
	 * This function gets the digit in a given binary number. 
	 * If the given index is out of bounds of the number then an error message will be displayed. 
	 * @param index
	 * @return digit in a given number 
	 */
	public int getDigit(int index) {
		if (index < 0 || index > data.length) {
			System.out.print("The index you have selected is out of bounds");
			return -1; 
		}
		else { 
			return data[index]; 
		}
		
	}
	
	/**
	 * This functions shift a binary number to the right "amount" times by placing 0's in front of 
	 * the binary number. 
	 * @param amount
	 */
	public void shiftR(int amount) {
		int prevLength = data.length;
		int newLength = prevLength + amount;
		
		int[] temp = new int[prevLength];					
		temp = data;																				
																									
		data = new int[newLength];							
		
		for (int x = 0; x < amount; x++) {					
			data[x] = 0;
		}
		
		for (int x = amount; x < newLength; x++) {			
			data[x] = temp[x - amount];
		}
		
		
		
	}
		
	
	/**
	 * This function adds two BinaryNumber objects and throws and error message if the lengths of the 
	 * numbers are not the same. 
	 * @param aBinaryNumber
	 */
	public void add(BinaryNumber aBinaryNumber) {
		if (aBinaryNumber.getLength() != data.length) {
			System.out.println("The binary numbers provided are not of equal length, therefore they cannot be added together.");
		}
		else {
			
			
			int temp[] = new int[data.length];									
			for (int x = 0; x < data.length; x++) {								
				temp[x] = 0;
			}
			
			
			for (int x = 0; x < data.length; x++) {							
				int paramNum = aBinaryNumber.getDigit(x);				
				int dataNum = data[x];
				int tempNum = temp[x];
				
				if (paramNum + dataNum + tempNum == 3) {			
					if (x + 1 == data.length) {									
						overflow = true;
						temp[x] = 1;
					}
					else {
						temp[x] = 1;
						temp[x + 1] = 1;
					}
				}
				else if (paramNum + dataNum + tempNum == 2) {		
					if (x + 1 == data.length) {									
						overflow = true;
						temp[x] = 0;
					}
					else {	
						temp[x] = 0;
						temp[x + 1] = 1;
					}
				}
				else if (paramNum + dataNum + tempNum == 1) {		
					temp[x] = 1;											
				}
				else {														
					temp[x] = 0;												
				}															
				
			}
			
			if (overflow == true) {									
				data = new int[data.length + 1];
				data[data.length] = 1;
			}
			
			for (int x = 0; x < data.length; x++) {
				data[x] = temp[x];
			}
		}
	}
	

	/**
	 * This function transform a binary number into a String and if the number is a result of 
	 * an overflow then "Overflow" will be displayed. 
	 */
	public String toString() {
		String str = ""; 
		for(int x = 0; x < data.length; x++) {
			str += data[x]; 
		}
		if (overflow == true) {
			return "Overflow"; 
		}
		else {
			return str; 
		}
		
	}
	
	/**
	 * This functions returns the decimal value of a given binary number. 
	 * This function uses the big-endian format 
	 * @return decimal equivalence to a given binary number 
	 */
	public int toDecimal() {
		int deci = 0; 
		for(int x = 0; x < data.length; x++) { 
			if (data[x] == 1) {
				deci += Math.pow(2, (data.length - x) - 1); 	
			}
		}
		
		return deci; 
	}
	
	/**
	 * This function clears the overflow flag. 
	 */
	public void clearOverflow() {
		overflow = false; 
	}
	
	public static void main(String args []) {
		
//		BinaryNumber num = new BinaryNumber(4); 
//		BinaryNumber num2 = new BinaryNumber("1010");
//		BinaryNumber num3 = new BinaryNumber("1000");
//		//System.out.println(num);
//		System.out.println(num2);
//		System.out.println(num2.getLength());
//		System.out.println(num2.getDigit(2));
//		System.out.println(num2.toDecimal());
//		num2.shiftR(3);
//		System.out.println(num2);
//		//num2.add(num3);
//		//System.out.println(num2);
		
	}

}
