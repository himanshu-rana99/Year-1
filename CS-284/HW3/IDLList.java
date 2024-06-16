package Homework3;

//Himanshu Rana 
//"I pledge my honor that I have abided by the Stevens Honor System"

import java.util.ArrayList;
import java.util.NoSuchElementException;

public class IDLList<E> {
	
	private static class Node<E> {
		E data; 
		Node<E> next; 
		Node<E> prev; 
		
		Node(E elem) {
			this.data = elem; 
			this.prev = null; 
			this.next = null; 
		}
		
		Node(E elem, Node<E> prev, Node<E> next) {
			this.data = elem; 
			this.prev = prev; 
			this.next = next; 
		}
		
		public String toString() {
			if(this.data == null) {
				return (String) null; 
			} else {
				return this.data.toString(); 
			}
		}
	}
	
	private Node<E> head; 
	private Node<E> tail; 
	private int size; 
	private ArrayList<Node<E>> indices;
	
	public IDLList() {
		head = null; 
		tail = null; 
		size = 0; 
		indices = new ArrayList<Node<E>>(); 
	}
	/**
	 * This function adds elem at the position index from where
	 * the head is
	 * @param index
	 * @param element
	 * @return boolean
	 */
	public boolean add(int index, E elem) {
		if (index > size || index < 0) {
			throw new IndexOutOfBoundsException(); 
		} else if (index == size) {
			append(elem); 
		} else if(index == 0) {
			add(elem); 
		} else {
			Node<E> prev = indices.get(index - 1);
			Node<E> temp = new Node<E>(elem, prev, prev.next);
			prev.next.prev = temp;
			prev.next = temp;
			indices.add(index, temp);
			size++;
		}
		return true; 
	
	}
	
	/**
	 * This function adds elem to the head and therefore 
	 * becomes the first element of the list
	 * @param elem
	 * @return boolean
	 */
	public boolean add(E elem) {
		if (head == null) {
			head = new Node<E>(elem);
			tail = head;
			indices.add(0, head);
			size++;
		} else {
			Node<E> prevHead = head;
			head = new Node<E>(elem, null, head);
			prevHead.prev = head;
			indices.add(0, head);
			size++;
		}
		
		return true;
	}
	
	/**
	 * This function adds an element to the end of a list.
	 * @param elem
	 * @return boolean value true
	 */
	public boolean append(E elem) {
		if (tail == null) {
			add(elem);
		} else {
			Node<E> prevTail = tail;
			tail = new Node<E>(elem, tail, null);
			prevTail.next = tail;
			indices.add(tail);
			size++;
		}
		
		return true;
	}
	
	/**
	 * This function returns the element at the given index
	 * @param 
	 * @return element of type E 
	 */
	public E get(int index) {
		return indices.get(index).data;
	}
	
	/**
	 * This function returns the head of the list.
	 * @return the head of the list
	 */
	public E getHead() {
		return head.data;
	}
	
	/**
	 * This function returns the tail of the list.
	 * @return the tail of the list
	 */
	public E getLast() {
		return tail.data;
	}
	
	/**
	 * Returns the size of a list.
	 * @return The size of a list
	 */
	public int size() {
		return size;
	}
	
	/**
	 * This function removes and returns the element at the head
	 * @return the head of the list 
	 */
	public E remove() {
		if (head == null) {
			throw new NoSuchElementException();
		}
		
		if(head == tail) {
			Node<E> temp = head;
			head = null;
			tail = null;
			indices.clear();
			size--;
			return temp.data;
		}
		
		Node<E> temp = head;
		head = head.next;
		indices.remove(0);
		size--;
		return temp.data;
	}
	
	/**
	 * This function removes and returns the element at the tail
	 * @return the tail of the list
	 */
	public E removeLast() {
		if (tail == null) {
			throw new NoSuchElementException();
		} else if (head == tail) {
			Node<E> temp = tail;
			head = null;
			tail = null;
			indices.clear();
			size--;
			return temp.data;
		} else {
			Node<E> temp = tail;
			tail = tail.prev;
			tail.next = null;
			indices.remove(size - 1);
			size--;
			return temp.data;
		}
	}
	/**
	 * This function removes the and return the element at the given index
	 * @param 
	 * @return element that was removed 
	 */	
	public E removeAt(int index) {
		if (head == null || tail == null) {
			throw new NoSuchElementException();
		}
		
		if (index < 0 || index >= size) {
			throw new IndexOutOfBoundsException();
		} else if (index == size - 1) {
			E elem = removeLast();
			return elem;
		} else if (index == 0) {
			E elem = remove();
			return elem;
		} else {
			Node<E> temp = indices.get(index);
			Node<E> prev = temp.prev;
			Node<E> next = temp.next;
			prev.next = next;
			next.prev = prev;			
			indices.remove(index);
			size--;
			return temp.data;
		}
	}
	
	/**
	 * This function removes the first occurrence of elem in the list
	 * @param 
	 * @return true if elem is in the list and false if it is not
	 */
	public boolean remove(E elem) {
		if (head == null) {
			throw new NoSuchElementException();
		}
		
		int index = 0;
		boolean IsInList = false;
		
		while(index < size && !IsInList) {
			if (indices.get(index).data.equals(elem)) {
				removeAt(index);
				IsInList = true;
			}
			else {
				index++;
			}
		}
		
		return IsInList;
	}
	
	/**
	 * This function presents a string representation of the list
	 * @return a string format of the list
	 */
	@Override
	public String toString() {
		String str = "[";
		
		if (head == null) {
			return "[]";
		}
		
		for (int i = 0; i < size - 1; i++) {
			str += indices.get(i).toString() + ",";
		}
		
		return str + indices.get(size - 1).toString() + "]";

	}
}
