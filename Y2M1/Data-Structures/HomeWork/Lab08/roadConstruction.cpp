#include <iostream>
#include <vector>
#include <queue>
#include <cstdio>

using namespace std;

class Graph{
    private:
        int vertices;
        int edges;
        vector<vector<int>> adjacent;

        void bfs(int start, vector<bool>& visited){
            queue<int> q;
            q.push(start);
            visited[start] = true;

            while(!q.empty()){
                int node = q.front();
                q.pop();

                for(int neighbor : adjacent[node]){
                    if(!visited[neighbor]){
                        q.push(neighbor);
                        visited[neighbor] = true;
                    }
                }
            }
        }
        
    public:
        Graph(int n) : vertices(n), edges(0){
            adjacent.resize(n);
        }
        void addEdge(int city1, int city2){
            adjacent[city1].push_back(city2);
            adjacent[city2].push_back(city1);
            edges++;
        }
        int getVertices() const{
            return vertices;
        }
        int getEdges() const{
            return edges;
        }
        int minimumRoad(){
            int group = 0;
            vector<bool> visited(vertices, false);

            for(int i = 0; i < vertices; ++i){
                if(!visited[i]){
                    bfs(i , visited);
                    group++;
                }
            }
            return group - 1;
        }
};

int main(){
    int allCity, road, city1, city2;

    // printf("Enter city and road: ");
    scanf("%d %d", &allCity, &road);

    Graph createGraph(allCity);

    for(int i = 0; i < road; ++i){
        // printf("Enter city1 and city2: ");
        scanf("%d %d", &city1, &city2);
        createGraph.addEdge(city1 -1, city2 -1);
    }

    int leastRoadToUse = createGraph.minimumRoad();
    printf("%d", leastRoadToUse);
}