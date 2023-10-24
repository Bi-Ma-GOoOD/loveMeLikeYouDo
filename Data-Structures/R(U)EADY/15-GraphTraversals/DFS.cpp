/* C++ program to print DFS traversal from a given vertec in given graph */
#include <iostream>
#include <list>
using namespace std;

//Graph class represents a undirected graph using adjacency list representation
class Graph{
    int V; // NO of vertices
    list<int>*adj; // Pointer to an array containing adjacency lists

    void DFSVisit(int s, bool visited[]); // recursive  function used by DFS
    void addEdge(int v, int w);
    void DFSInit(int s);
};

// Graph::Graph(int V){
//     this->V = V;
//     adj = new list<int>[V];
// }

void Graph::addEdge(int v, int w){
    adj[v].push_back(w); // Add w to v's list
    adj[w].push_back(v); // Add v to w's list
}

void Graph::DFSVisit(int s, bool visited[]){
    // Mark the current node as visited and print it
    visited[s] = true;
    cout << s << " ";

    //Recurse for all the vertices adjacent to this vertex
    list<int>::iterator i;
    for(i = adj[s].begin(); i != adj[s].end(); ++i)
        if(!visited[*i])
            DFSVisit(*i, visited);
}

//DFS traversal of the vertices reachable from v
void Graph::DFSInit(int s){
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    for(int i = 0 ; i < V; i++)
        visited[i] = false;

    //Call the recursive helper funtion to print DFS traversal
    DFSVisit(s, visited);
}

int main(){
    // Graph g(4);
    // g.addEdge(0, 1);
    // g.addEdge(0, 2);
    // g.addEdge(1, 2);
    // g.addEdge(2, 0);
    // g.addEdge(2, 3);
    // cout << "Following is Depth First Traversal (starting from vertex 2) \n";
    // g.DFSInit(2);
    // return 0;
}