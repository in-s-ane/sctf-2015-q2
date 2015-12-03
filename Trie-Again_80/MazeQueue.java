public class MazeQueue {

    private Node[] q;

    public MazeQueue() {
        q = new Node[0];
    }

    public void add(Node n) {
        Node[] tmp = new Node[q.length + 1];
        System.arraycopy(q , 0 , tmp , 0 , q.length);
        tmp[q.length] = n;
        q = tmp;
    }

    public Node pop() {
        Node retVal = q[0];
        Node[] tmp = new Node[q.length - 1];
        System.arraycopy(q , 1 , tmp , 0 , q.length - 1);
        q = tmp;
        return retVal;
    }

    public Node peek() {
        return q[0];
    }

    public boolean empty() {
        return q.length == 0;
    }
}
