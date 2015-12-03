public class Driver {
    public static void main(String[] args) {
        long startTime , endTime;

        // Warm up JVM for time testing
        for (int i = 0 , a = 0; i < 100000; i++) {
            a += 1;
        }

        BFSMaze solver = new BFSMaze();
        startTime = System.nanoTime();
        solver.run();
        endTime = System.nanoTime() - startTime;

        System.out.println("Solved in " + nanoToMillis(endTime) + " milliseconds.");
    }

    private static String nanoToMillis(long nano) {
        String tmp = Long.toString(nano);
        while (tmp.length() < 6) {
            tmp = "0" + tmp;
        }
        return tmp.substring(0 , tmp.length() - 6) + "." + tmp.substring(tmp.length() - 6);
    }
}
