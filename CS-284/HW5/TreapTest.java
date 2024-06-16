package Homework5;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

//"I pledge my honor that I have abided by the Stevens Honor System" - Himanshu Rana 

class TreapTest {

	@Test
	public void addTest() {
		Treap<Integer> testTree = new Treap<Integer>();
		testTree.add(4,19);
		testTree.add(2,31);
		testTree.add(6,70);
		testTree.add(1,84);
		testTree.add(3,12);
		testTree.add(5,83);
		testTree.add(7,26);
		
		
	}
	
	@Test
	public void deleteTest() {
		Treap<Integer> testTree = new Treap<Integer>();
		testTree.add(4,19);
		testTree.add(2,31);
		testTree.add(6,70);
		testTree.add(1,84);
		testTree.add(3,12);
		testTree.add(5,83);
		testTree.add(7,26);
		testTree.delete(3);
		
		
	}
	
	@Test
	public void findTest() {
		Treap<Integer> testTree = new Treap<Integer>();
		testTree.add(4,19);
		testTree.add(2,31);
		testTree.add(6,70);
		testTree.add(1,84);
		testTree.add(3,12);
		testTree.add(5,83);
		testTree.add(7,26);
		testTree.find(1);
	}

}
