package Homework6;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

//Himanshu Rana 
//"I pledge my honor that I have abided by the Stevens Honor System" 


import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;


class AnagramsTest {

	@Test
	public void testBuildLetterTable() {
		Anagrams a = new Anagrams();
		System.out.println(a.letterTable);
		assertEquals(a.letterTable.toString(),"{a=2, b=3, c=5, d=7, e=11, f=13, g=17, h=19, i=23, j=29, k=31, l=37, m=41, n=43, o=47, p=53, q=59, r=61, s=67, t=71, u=73, v=79, w=83, x=89, y=97, z=101}");

	}
	
	@Test
	public void testAddWord() {
		Anagrams a = new Anagrams();
		
		a.addWord("bat");
		a.addWord("table");
		
		boolean check = false;
		for(Map.Entry<Long, ArrayList<String>> entry : a.anagramTable.entrySet()) {
			if(entry.getValue().get(0).equals("bat") || entry.getValue().get(0).equals("table")){
				check = true;
			}
		}
		assertEquals(Boolean.toString(check),"true");
	}
	
	@Test
	public void testMyHashCode() {
		Anagrams a = new Anagrams();
		boolean correct = false;
		if(a.myHashCode("bat") == (long) 485194){
			correct = true;
		}
		assertEquals(Boolean.toString(correct), "true");
	}
	
	
	
	
	

}

