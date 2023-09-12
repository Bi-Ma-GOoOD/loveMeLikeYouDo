#include <iostream>
#include <vector>
using namespace std;

vector<int>* createGraph(int n);
void addEdge(vector<int>* adjlist, int u, int v);
bool isAdjacent(vector<int>* adjlist, int u, int v);

int main(){
    int vertices, edges, node1, node2;
    int i, j;

    // printf("Enter vertices and edges: ");
    scanf("%d %d",&vertices, &edges);

    vector<int>* adjlist = createGraph(vertices);

    for(i = 0; i < edges; ++i){
        // printf("Enter addEdge: ");
        scanf("%d %d", &node1 , &node2);
        addEdge(adjlist, node1, node2);
    }

    for(j = 0; j < vertices; ++j){
        bool check = isAdjacent(adjlist, j, 1);
        if(check == true){
            // printf("No, this is't tree");
            printf("NO");
            return 0;
        }else{
            // printf("Yes, this is tree.");
            printf("YES");
            return 0;
        }
    }
}

vector<int>* createGraph(int n){
    return new vector<int>[n];
}
void addEdge(vector<int>* adjlist, int u, int v){
    adjlist[u].push_back(v);
}
bool isAdjacent(vector<int>* adjList, int u, int v){
    for(int i = 0; i < (int)adjList[u].size(); ++i){
        if(adjList[u].at(i) == v){
            return true;
        }
    }
    return false;
}