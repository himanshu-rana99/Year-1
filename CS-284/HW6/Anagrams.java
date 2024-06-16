package Homework6;

import java.io.BufferedReader;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;


//Himanshu Rana 
//"I pledge my honor that I have abided by the Stevens Honor System" 

public class Anagrams {
	
	final Integer[] primes = {2, 3 , 5 , 7, 11 , 13 , 17 , 19 , 23 , 29 , 
							  31 , 37 , 41 , 43 , 47 , 53 , 59 , 61 ,
			                  67 , 71 , 73 , 79 , 83 , 89 , 97 , 101};
	Map<Character, Integer> letterTable; 
	Map<Long, ArrayList<String>> anagramTable; 
	
	public Anagrams() {
		anagramTable = new HashMap<Long, ArrayList<String>>(); 
		buildLetterTable(); 
	}
	
	/**
	 * This function is invoked by the constructor and builds the hash table letterTable 
	 * that assigns each letter to its corresponding prime number 
	 */
	private void buildLetterTable() {
		letterTable = new HashMap<Character, Integer>()
		{{ 
		     put('a', 2);
		     put('b', 3);
		     put('c', 5);
		     put('d', 7);
		     put('e', 11);
		     put('f', 13);
		     put('g', 17);
		     put('h', 19);
		     put('i', 23);
		     put('j', 29);
		     put('k', 31);
		     put('l', 37);
		     put('m', 41);
		     put('n', 43);
		     put('o', 47);
		     put('p', 53);
		     put('q', 59);
		     put('r', 61);
		     put('s', 67);
		     put('t', 71);
		     put('u', 73);
		     put('v', 79);
		     put('w', 83);
		     put('x', 89);
		     put('y', 97);
		     put('z', 101);    
		}};
	}
	
	/**
	 * This function computes the hash code for each string and adds this word
	 *  to the hash table anagramTable 
	 * @param s
	 */
	private void addWord(String s) {
		long code = myHashCode(s); 
		
		if(anagramTable.get(code) == null) {
			anagramTable.put(code, new ArrayList<String>());
		}
		
		anagramTable.get(code).add(s);
	}
	
	/**
	 * This function computes the hash code for each entry by using the 
	 * fundamental theorem of arithmetic 
	 * @param s
	 * @return
	 */
	private Long myHashCode(String s) {
		if(s == null) {
			throw new IllegalArgumentException(); 
		} else {
			long code = 1; 
			for(int i = 0; i < s.length(); i++) {
				code = code*(long)letterTable.get(s.charAt(i));
			}
			return code; 
		}
	}
	/**
	 * This function receives the name of a text file that contains 
	 * words and builds the hash table
	 * @param s
	 * @throws IOException
	 */
	public void proccessFile (String s) throws IOException {
		FileInputStream fstream = new FileInputStream(s); 
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
		String strLine; 
		while((strLine = br.readLine()) != null) {
			this.addWord(strLine);
		}
		br.close();
	}
	
	/**
	 * 
	 * @return a list of the entries in anagramTable that have the 
	 * largest number of anagrams 
	 */
	private ArrayList<Map.Entry<Long, ArrayList<String>>> getMaxEntries() {
		ArrayList<Map.Entry<Long,ArrayList<String>>> maxAnagrams = new ArrayList<HashMap.Entry<Long,ArrayList<String>>>();
		if(anagramTable.isEmpty()){
			return null;
		} else {
			maxAnagrams.add(anagramTable.entrySet().iterator().next());
		}
		for(Map.Entry<Long, ArrayList<String>> entry : anagramTable.entrySet()) { 
			boolean IfInTable = false;
			for (int i = 0; i < maxAnagrams.size(); i++){ 
				if(((entry.getValue()).equals(maxAnagrams.get(i).getValue()))) {
					IfInTable = true;
				}
			}
			if(maxAnagrams.get(0).getValue().size() == entry.getValue().size() && !IfInTable) { 
				maxAnagrams.add(entry);
			} else if(!IfInTable && maxAnagrams.get(0).getValue().size() < entry.getValue().size()) { 
				maxAnagrams.clear();
				maxAnagrams.add(entry);
			}
		}
		return maxAnagrams;
	}
	
	public static void main (String[] args) {
		Anagrams a = new Anagrams(); 
		
		final long startTime = System.nanoTime(); 
		try {
			a.proccessFile("words_alpha.txt");
		} catch (IOException e1) {
			e1.printStackTrace(); 
		}
		
		ArrayList<Map.Entry<Long, ArrayList<String>>> maxEntries = a.getMaxEntries();
		final long estimatedTime = System.nanoTime() - startTime; 
		final double seconds = ((double) estimatedTime/1000000000); 
		System.out.println("Time: " + seconds); 
		System.out.println("Key of max anagrams: "  + maxEntries.get(0).getKey());  //+ something
		System.out.println("List of max anagrams: " +  maxEntries.get(0).getValue());
		System.out.println("Length of list of max anagrams: " + maxEntries.get(0).getValue().size()); // + something
	}
	
	
	

}
