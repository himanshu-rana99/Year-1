package Homework5;

import java.util.Random; 
import java.util.Stack; 

//"I pledge my honor that I have abided by the Stevens Honor System" - Himanshu Rana 


public class Treap<E extends Comparable<E>> {
	
	private static class Node<E> {
		public E data; 
		public int priority; 
		public Node<E> left; 
		public Node<E> right; 
		
		//constructor
		public Node(E data, int priority) {
			if(data == null) {
				throw new NullPointerException(); 
			}
			
			this.data = data; 
			this.priority = priority; 
		}
		
		//methods
		Node<E> rotateRight() {
			Node<E> left1 = this.left; 
			Node<E> right1 = this.right; 
			left1.right = this; 
			this.left = right1; 
			return left1; 
		}
		
		Node<E> rotateLeft() {
			Node<E> right1 = this.right; 
			Node<E> left1 = this.left; 
			right1.left = this; 
			this.right = left1; 
			return right1; 
		}	
		
	}
	
	private Random priorityGenerator; 
	private Node<E> root; 
	
	
	//constructor
	public Treap() {
		this.priorityGenerator = new Random(); 
		root = null; 
	}
	
	public Treap(long seed) {
		this.priorityGenerator = new Random(seed); 
		root = null;  
	}
	
	//methods
	/**
	 * This function inserts the given element into the tree by creating a new node containing the key and a random priority.  
	 * @param key
	 * @return true if successfully added a new node and false if it does not modify the treap
	 */
	boolean add(E key) {
		int prioGen = this.priorityGenerator.nextInt(10); 
		return add(key, prioGen); 
	}
	
	boolean add(E key, int priority) {
		Node<E> addition = new Node<E>(key, priority); 
		if(this.root == null) {
			this.root = addition; 
			return true; 
		}
		Stack<Node<E>> path = new Stack<Node<E>>(); 
		Node<E> curr = this.root; 
		path.push(curr); 
		while(curr != null) {
			if(addition.data.compareTo(curr.data) > 0) {
				if(curr.right == null) {
					curr.right = addition; 
					reheap(path, addition); 
					return true; 
				}
				curr = curr.right; 
				path.push(curr); 
				
			}
			if(addition.data.compareTo(curr.data)<0) {
				if(curr.left == null) {
					curr.left = addition; 
					reheap(path, addition); 
					return true; 
				}
				curr = curr.left; 
				path.push(curr); 
			}
		}
		return false; 
	}
	
	/**
	 * This functions helps to restore the heap into its correct order once a new node is inserted 
	 * @param path
	 * @param addition
	 */
	private void reheap(Stack<Node<E>> path, Node<E> addition) {
		while(!path.isEmpty()) {
			Node<E> x = path.pop(); 
			if(x.priority > addition.priority) {
				break; 
			} else {
				if(addition.data.compareTo(x.data) > 0) {
					addition = x.rotateLeft(); 
				} else {
					addition = x.rotateRight(); 
				}
				if(!path.isEmpty()) {
					Node<E> y = path.peek(); 
					if(y.left == x) {
						y.left = addition; 
					} else {
						y.right = addition; 
					}
				} else {
					this.root = addition; 
				}
			}
		}
			
	}
	
	/**
	 * This function deletes the node with the given key from the treap 
	 * @param key
	 * @return true is node was succesfully deleted and false if it does not modify the treap 
	 */
	boolean delete(E key) {
		if(this.root == null || this.find(key) == false || key == null) {
			return false; 
		} else {
			this.root = delete_helper(this.root, key); 
			return true; 
		}
		
	}
	
	public Node<E> delete_helper(Node<E> curr, E key) {
		if(curr == null) {
			return null; 
		}
		if(key.compareTo(curr.data) > 0){
			curr.right = delete_helper(curr.right, key);
		} else if(key.compareTo(curr.data) < 0){
			curr.left = delete_helper(curr.left, key);
		} else if(curr.right == null) {
			Node<E> diff = curr.left;
			curr = diff;
		} else if(curr.left == null) {
			Node<E> diff = curr.right;
			curr = diff;
		} else if(curr.right.priority > curr.left.priority) {
			curr = curr.rotateLeft();
			curr.left = delete_helper(curr.left, key);
		} else if(curr.right.priority < curr.left.priority) {
			curr = curr.rotateRight();   
			curr.right = delete_helper(curr.right, key);
		}
		return curr;
		
	}
	
	/**
	 * This function finds a node with the given key in the treap rooted at the root
	 * @param root
	 * @param key 
	 * @return true if it finds the node and false if it doesn't 
	 */
	private boolean find(Node<E> root, E key) {
		if(this.root.data == key) {
			return true; 
		}
		
		Node<E> curr = root; 
		while(curr != null) {
			if(key.compareTo(curr.data) < 0) {
				curr = curr.left; 
				if(key.compareTo(curr.data) == 0) {
					return true; 
				}
			}
			if(key.compareTo(curr.data) > 0) {
				curr = curr.right; 
				if(key.compareTo(curr.data) == 0) {
					return true; 
				}
			}
		}
		return false; 
	}
	
	/**
	 * This function finds a node with the given key in the treap 
	 * @param key
	 * @return true if it finds it and false if it doesn't  
	 */
	public boolean find(E key) {
		if(this.root.data == key) {
			return true; 
		}
		
		Node<E> curr = this.root; 
		while(curr != null) {
			if(key.compareTo(curr.data) < 0) {
				curr = curr.left; 
				if(key.compareTo(curr.data) == 0) {
					return true; 
				}
			}
			if(key.compareTo(curr.data) > 0) {
				curr = curr.right; 
				if(key.compareTo(curr.data) == 0) {
					return true; 
				}
			}
		}
		return false; 
	}
	
	/**
	 * This function orients the treap using the pre-order method 
	 * @param node
	 * @param depth
	 * @param sb
	 */
	private void preOrderTraversal(Node<E> node, int depth, StringBuilder sb) {
		for(int x = 1; x < depth; x++) {
			sb.append(" ");
		}
		if(node == null) {
			sb.append("node is null");
		} else {
			sb.append(node.toString());
			sb.append("\n");
			preOrderTraversal(node.left, depth + 1, sb);
			preOrderTraversal(node.right, depth + 1, sb);
		}
	}
	public String toString() {
		StringBuilder sb = new StringBuilder(); 
		preOrderTraversal(root, 1, sb); 
		return sb.toString();
	}
	
	
	

}
