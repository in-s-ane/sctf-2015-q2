import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

public class BFSMaze {

    private static final char VISITED = '.';

    private char[][] grid;
    private MazeQueue queue;
    private ArrayList<String> words;
    private ArrayList<String> matches;

    public BFSMaze() {
        try {
            matches = new ArrayList<String>();
            Scanner ifstream = new Scanner(new File("words.txt"));
            ArrayList<String> dict = new ArrayList<String>();
            while (ifstream.hasNext()) {
                String word = ifstream.nextLine().trim().toUpperCase();
                if (word.matches("[ECALPHNBOQTY]+") && ! dict.contains(word)) {
                    dict.add(word);
                }
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

    public int solve(int[] startCoor, String key) {
        Node current = null;
        Node buffer = new Node(startCoor[0] , startCoor[1], "");

        buffer.setParent(null);
        queue.add(buffer);
        char ELEMENT = ' ';
        // Reset grid
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
                System.out.printf("Matched: %s\n", tmp);
                return 1;
            } else if ((tmp+"LEE").equals(key)) {
                // LEE never matches...
                System.out.printf("Hack matched: %s\n", tmp+"LEE");
                return 1;
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
            Node iter4 = new Node(current.r - 1 , current.c - 1, tmp);
            Node iter7 = new Node(current.r - 1, current.c + 1, tmp);
            Node iter6 = new Node(current.r + 1, current.c - 1, tmp);
            Node iter5 = new Node(current.r + 1 , current.c + 1, tmp);
            iter0.setParent(current);
            iter1.setParent(current);
            iter2.setParent(current);
            iter3.setParent(current);
            iter4.setParent(current);
            iter5.setParent(current);
            iter6.setParent(current);
            iter7.setParent(current);
            queue.add(iter0);
            queue.add(iter1);
            queue.add(iter2);
            queue.add(iter3);
            queue.add(iter4);
            queue.add(iter5);
            queue.add(iter6);
            queue.add(iter7);
        }
        return 0;
    }

    public void run() {
        int total = 0;
        for (int i = 0; i < words.size(); i++) {
            if (i % 500 == 0) {
                System.out.printf("Word: %d / %d. Current sum: %d\n", i, words.size(), total);
            }
            int sum = 0;
            String word = words.get(i);
            switch (word.charAt(0)) {
                case 'A':
                    sum += solve(new int[]{0,3}, word);
                    sum += solve(new int[]{1,0}, word);
                    break;
                case 'B':
                    sum += solve(new int[]{2,2}, word);
                    break;
                case 'C':
                    sum += solve(new int[]{0,2}, word);
                    break;
                case 'E':
                    sum += solve(new int[]{0,0}, word);
                    sum += solve(new int[]{0,1}, word);
                    sum += solve(new int[]{1,2}, word);
                    break;
                case 'H':
                    sum += solve(new int[]{2,0}, word);
                    break;
                case 'L':
                    sum += solve(new int[]{1,1}, word);
                    break;
                case 'N':
                    sum += solve(new int[]{2,1}, word);
                    break;
                case 'O':
                    sum += solve(new int[]{2,3}, word);
                    break;
                case 'P':
                    sum += solve(new int[]{1,3}, word);
                    break;
                case 'Q':
                    sum += solve(new int[]{3,0}, word);
                    break;
                case 'T':
                    sum += solve(new int[]{3,1}, word);
                    sum += solve(new int[]{3,2}, word);
                    break;
                case 'Y':
                    sum += solve(new int[]{3,3}, word);
                    break;
                default:
                    break;
            }
            if (sum != 0) {
                matches.add(word);
                total += 1;
            }
        }
        System.out.println(total);
        System.out.println(matches);
    }
}
