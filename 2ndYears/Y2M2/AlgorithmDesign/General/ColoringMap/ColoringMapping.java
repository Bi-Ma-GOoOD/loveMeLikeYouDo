public class ColoringMapping {

    public static void main(String[] args) {

        ColoringMapping m = new ColoringMapping();

        m.createMap();

        boolean result = m.explore(0, RED);
        if (result) {
            System.out.println("OK");
        } else {
            System.out.println("NO");
        }

        m.printMap();

    }

    private void createMap() {
        map = new int[7][];
        map[0] = new int[] {1, 4, 2, 5};
        map[1] = new int[] {0, 4, 6, 5};
        map[2] = new int[] {0, 4, 3, 6, 5};
        map[3] = new int[] {2, 4, 6};
        map[4] = new int[] {0, 1, 6, 3, 2};
        map[5] = new int[] {2, 6, 1, 0};
        map[6] = new int[] {2, 3, 4, 1, 5};
    }

    private boolean explore(int country, int color) {

        if (country >= map.length) {
            // Check if all countries are colored
            for (int i = 0; i < mapColors.length; i++) {
                if (mapColors[i] == NONE) {
                    return false; // Not all countries are colored
                }
            }
            return true; // All countries are colored
        }

        if (okToColor(country, color)) {
            mapColors[country] = color;
            // Try all possible colors for the next country
            for (int nextColor = RED; nextColor <= BLUE; nextColor++) {
                if (explore(country + 1, nextColor)) {
                    return true; // Successfully colored all countries
                }
            }
            // Backtrack if coloring with the current color leads to a dead end
            mapColors[country] = NONE; // Reset the color for backtracking
        }
        return false;
    }

    private boolean okToColor(int country, int color) {
        for(int i = 0; i < map[country].length; i++){
            int ithAdjCountry = map[country][i];
            if(mapColors[ithAdjCountry] == color){
                return false;
            }
        }
        return true;
    }

    private void printMap() {
        for(int i = 0; i < mapColors.length; i++){
            System.out.println("map[" + i + "] is ");
            switch (mapColors[i]) {
                case NONE:
                    System.out.println("none");
                    break;
                case RED:
                    System.out.println("red");
                    break;
                case YELLOW:
                    System.out.println("yellow");
                    break;
                case GREEN:
                    System.out.println("green");
                    break;
                case BLUE:
                    System.out.println("blue");
                    break;
            }
        }
    }

    private static final int NONE = 0;
    private static final int RED = 1;
    private static final int YELLOW = 2;
    private static final int GREEN = 3;
    private static final int BLUE = 4;
    int[][] map;
    int[] mapColors = {NONE, NONE, NONE, NONE, NONE, NONE, NONE};

    public ColoringMapping() {
        map = new int[7][];
    }
}

