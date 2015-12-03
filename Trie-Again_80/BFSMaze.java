import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;

public class BFSMaze {

    private static final char VISITED = '.';

    private char[][] grid;
    private MazeQueue queue;
    private ArrayList<String> words;

    public BFSMaze() {
        try {
            Scanner ifstream = new Scanner(new File("words.txt"));
            ArrayList<String> dict = new ArrayList<String>();
            while (ifstream.hasNext()) {
                dict.add(ifstream.nextLine().trim().toUpperCase());
            }
            ifstream.close(); ifstream = null;
            words = dict;
        } catch(Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
        queue = new MazeQueue();
        grid = new char[4][4];
        grid[0][0] = 'E';
        grid[0][1] = 'E';
        grid[0][2] = 'C';
        grid[0][3] = 'A';
        grid[1][0] = 'A';
        grid[1][1] = 'L';
        grid[1][2] = 'E';
        grid[1][3] = 'P';
        grid[2][0] = 'H';
        grid[2][1] = 'N';
        grid[2][2] = 'B';
        grid[2][3] = 'O';
        grid[3][0] = 'Q';
        grid[3][1] = 'T';
        grid[3][2] = 'T';
        grid[3][3] = 'Y';
    }

    public boolean solve(int[] startCoor, String key) {
        Node current = null;
        Node buffer = new Node(startCoor[0] , startCoor[1], "");

        buffer.setParent(null);
        queue.add(buffer);
        char ELEMENT = ' ';
        while (!queue.empty()) {
            current = queue.pop();
            if (
                    current.r < 0 ||
                    current.c < 0 ||
                    current.r >= grid.length ||
                    current.c >= grid[0].length
                    ) {
                continue;
            }
            ELEMENT = grid[current.r][current.c];
            String tmp = current.built + ELEMENT;
            if (tmp.equals(key)) {
                System.out.printf("\tMatched: %s\n", tmp);
                return true;
            }
            if (ELEMENT == VISITED) {
                continue;
            }
            if (tmp.length() > key.length()) {
                continue;
            }
            if (!tmp.equals(key.substring(0, tmp.length()))) {
                continue;
            }

            grid[current.r][current.c] = VISITED;
            Node iter0 = new Node(current.r - 1 , current.c, tmp);
            Node iter1 = new Node(current.r + 1 , current.c, tmp);
            Node iter2 = new Node(current.r , current.c - 1, tmp);
            Node iter3 = new Node(current.r , current.c + 1, tmp);
            iter0.setParent(current);
            iter1.setParent(current);
            iter2.setParent(current);
            iter3.setParent(current);
            queue.add(iter0);
            queue.add(iter1);
            queue.add(iter2);
            queue.add(iter3);
        }
        return false;
    }

    public void run() {
        int total = 0;
        for (int i = 0; i < words.size(); i++) {
            if (i % 500 == 0) {
                System.out.printf("Word: %d / %d. Current sum: %d\n", i, words.size(), total);
            }
            switch (words.get(i).charAt(0)) {
                case 'A':
                    total += solve(new int[]{0,3}, words.get(i)) ? 1 : 0;
                    total += solve(new int[]{1,0}, words.get(i)) ? 1 : 0;
                    break;
                case 'B':
                    total += solve(new int[]{2,2}, words.get(i)) ? 1 : 0;
                    break;
                case 'C':
                    total += solve(new int[]{0,3}, words.get(i)) ? 1 : 0;
                    break;
                case 'E':
                    total += solve(new int[]{0,0}, words.get(i)) ? 1 : 0;
                    total += solve(new int[]{0,1}, words.get(i)) ? 1 : 0;
                    total += solve(new int[]{1,2}, words.get(i)) ? 1 : 0;
                    break;
                case 'H':
                    total += solve(new int[]{2,0}, words.get(i)) ? 1 : 0;
                    break;
                case 'L':
                    total += solve(new int[]{1,1}, words.get(i)) ? 1 : 0;
                    break;
                case 'N':
                    total += solve(new int[]{2,1}, words.get(i)) ? 1 : 0;
                    break;
                case 'O':
                    total += solve(new int[]{2,3}, words.get(i)) ? 1 : 0;
                    break;
                case 'P':
                    total += solve(new int[]{1,3}, words.get(i)) ? 1 : 0;
                    break;
                case 'Q':
                    total += solve(new int[]{3,0}, words.get(i)) ? 1 : 0;
                    break;
                case 'T':
                    total += solve(new int[]{3,1}, words.get(i)) ? 1 : 0;
                    total += solve(new int[]{3,2}, words.get(i)) ? 1 : 0;
                    break;
                case 'Y':
                    total += solve(new int[]{3,3}, words.get(i)) ? 1 : 0;
                    break;
                default:
                    break;
            }
        }
    }
}
