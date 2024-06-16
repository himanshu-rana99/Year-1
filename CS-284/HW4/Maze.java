package Maze;

/**
 * Class that solves maze problems with backtracking.
 * @author Koffman and Wolfgang
 * 
 * @author Himanshu Rana 
 * "I pledge my honor that I have abided by the Stevens Honor System" - Himanshu Rana 
 **/

import java.util.ArrayList; 
import java.util.Stack; 


public class Maze implements GridColors {

    /** The maze */
    private TwoDimGrid maze;

    public Maze(TwoDimGrid m) {
        maze = m;
    }

    /** Wrapper method. */
    public boolean findMazePath() {
        return findMazePath(0, 0); // (0, 0) is the start point.
    }

    /**
     * Attempts to find a path through point (x, y).
     * @pre Possible path cells are in BACKGROUND color;
     *      barrier cells are in ABNORMAL color.
     * @post If a path is found, all cells on it are set to the
     *       PATH color; all cells that were visited but are
     *       not on the path are in the TEMPORARY color.
     * @param x The x-coordinate of current point
     * @param y The y-coordinate of current point
     * @return If a path through (x, y) is found, true;
     *         otherwise, false
     */
    public boolean findMazePath(int x, int y) {
        if(x >= maze.getNCols() || y >= maze.getNRows() || x < 0 || y < 0) {
        	return false; 
        }
        
        if(!maze.getColor(x, y).equals(NON_BACKGROUND) || maze.getColor(x, y).equals(PATH)) {
        	return false; 
        }
        
        if(x == maze.getNCols() - 1 || y == maze.getNRows() - 1) {
        	maze.recolor(x, y, PATH);
        	return true; 
        } else {
        	maze.recolor(x, y, PATH);
        }
        
        if(findMazePath(x, y - 1) || findMazePath(x + 1, y) || findMazePath(x - 1, y) || findMazePath(x, y +1)) {
        	return true; 
        } else {
        	maze.recolor(x, y, TEMPORARY);
        	return false; 
        }
    }


    public ArrayList<ArrayList<PairInt>> findAllMazePaths(int x, int y) {
    	ArrayList<ArrayList<PairInt>> result = new ArrayList<>(); 
    	Stack<PairInt> trace = new Stack<>(); 
    	findMazePathStackBased(0, 0, result, trace); 
    	return result; 
    }
    
    public void findMazePathStackBased(int x, int y, ArrayList<ArrayList<PairInt>> result, Stack<PairInt> trace) {
    	if(x >= maze.getNCols() || y >= maze.getNRows() || x < 0 || y < 0) {
    		return; 
    	}
    	
    	if(maze.getColor(x, y).equals(NON_BACKGROUND)) {
    		return; 
    	}
    	
    	if(x == maze.getNCols() - 1 || y == maze.getNRows() - 1) {
    		PairInt pair = new PairInt(x, y); 
    		ArrayList<PairInt> z = new ArrayList<PairInt>(); 
    		z.addAll(trace); 
    		z.add(pair); 
    		result.add(z); 
    		return; 
    	} else {
    		maze.recolor(x, y, PATH);
    		PairInt z = new PairInt(x, y); 
    		trace.push(z); 
    		findMazePathStackBased(x - 1, y, result, trace); 
    		findMazePathStackBased(x, y - 1, result, trace); 
    		findMazePathStackBased(x, y - 1, result, trace); 
    		findMazePathStackBased(x + 1, y, result, trace); 
    		trace.pop(); 
    		maze.recolor(x,  y, NON_BACKGROUND);
    		return; 
    	}
    }
    
        
    public ArrayList<PairInt> findMazePathMin(int x, int y) {
    	maze.recolor(PATH, NON_BACKGROUND);
    	ArrayList<ArrayList<PairInt>> answer = findAllMazePaths(x, y);
    	if(answer.size() != 0) {
    		ArrayList<PairInt> min = answer.get(0); 
    		int minLength = min.size(); 
    		for(int a = 1; a < answer.size(); a++) {
    			if(minLength >= answer.get(a).size()) {
    				min = answer.get(a); 
    				minLength = min.size(); 
    				
    			}
    		}
    		return min;
    	} else {
    		return new ArrayList<PairInt>(); 
    	}
    	
    }

    /*<exercise chapter="5" section="6" type="programming" number="2">*/
    public void resetTemp() {
        maze.recolor(TEMPORARY, BACKGROUND);
    }
    /*</exercise>*/

    /*<exercise chapter="5" section="6" type="programming" number="3">*/
    public void restore() {
        resetTemp();
        maze.recolor(PATH, BACKGROUND);
        maze.recolor(NON_BACKGROUND, BACKGROUND);
    }
    /*</exercise>*/
}
/*</listing>*/
