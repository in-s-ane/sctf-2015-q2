public class Node {

    public int r;
    public int c;
    public String built;

    private Node parent;

    public Node() {
        r = -1;
        c = -1;
        parent = null;
    }

    public Node(int x , int y, String s) {
        r = x;
        c = y;
        built = s;
        parent = null;
    }

    public void setParent(Node n) {
        parent = n;
    }

    public Node getParent() {
        return parent;
    }

}
