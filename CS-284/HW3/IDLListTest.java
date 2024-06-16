package Homework3;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class IDLListTest {

	@Test
	public void testAdd() {
		IDLList<Integer> list = new IDLList<Integer>();
		list.add(1);
		assertEquals("[1]", list.toString());
		list.add(2);
		assertEquals("[2,1]", list.toString());
		
	}
	
	@Test
	public void testIndexedAdd() {
		IDLList<String> list = new IDLList<String>();
		list.add(0, "Honda");
		assertEquals("[Honda]", list.toString());	
		list.add("Toyota");
		list.add("Mazda");
		list.add(1, "Ford");
		assertEquals("[Mazda,Ford,Toyota,Honda]", list.toString());
		}
	
	@Test
	public void testAppend() {
		IDLList<Character> list = new IDLList<Character>();
		list.append('A');
		assertEquals("[A]", list.toString());
		list.append('B');
		assertEquals("[A,B]", list.toString());
	}
	
	@Test
	public void testGet() {
		IDLList<String> list = new IDLList<String>();
		list.add("blue");
		list.add("red");
		list.add("green");
		assertSame("blue", list.get(2));
		assertSame("green", list.get(0));
	}
	
	@Test
	public void testGetHead() {
		IDLList<Integer> list = new IDLList<Integer>();
		list.append(1);
		list.append(2);
		list.append(3);
		assertSame(1, list.getHead());

	}
	
	@Test
	public void testGetLast() {
		IDLList<Integer> list = new IDLList<Integer>();
		list.add(1);
		list.add(2);
		list.append(3);
		assertSame(3, list.getLast());
		
	}
	
	@Test
	public void testSize() {
		IDLList<Integer> list = new IDLList<Integer>();
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		assertSame(4, list.size());
	
	}
	
	@Test
	public void testRemove() {
		IDLList<Integer> list = new IDLList<Integer>();
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(3);
		list.remove();
		assertEquals("[3,2,1]", list.toString());
		list.append(0);
		list.remove();
		assertEquals("[2,1,0]", list.toString());
	}
	
	@Test
	public void testRemoveLast() {
		IDLList<Character> list = new IDLList<Character>();
		list.add('1');
		list.removeLast();
		assertEquals("[]", list.toString());
		list.add('2');
		list.add('3');
		list.add('4');
		list.removeLast();
		assertEquals("[4,3]", list.toString());
		
	}
	
	@Test
	public void testRemoveAt() {
		IDLList<Integer> list = new IDLList<Integer>();
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		list.removeAt(2);
		assertEquals("[5,4,2,1]", list.toString());
		
			
	}
	
	@Test
	public void testRemoveElement() {
		IDLList<Integer> list = new IDLList<Integer>();
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		assertEquals(true, list.remove(2));
		assertEquals("[5,4,3,1]", list.toString());
		list.add(6);
		assertEquals(true, list.remove(3));
		assertEquals("[6,5,4,1]", list.toString());

	}

}