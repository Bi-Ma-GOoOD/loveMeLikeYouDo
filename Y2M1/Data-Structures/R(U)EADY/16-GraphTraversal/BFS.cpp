/* C++ program to print BFS traversal from a given vertec in given graph */
#include <iostream>
#include <list>
using namespace std;

//Graph class represents a undirected graph using adjacency list representation
class Graph{
    int V; // NO of vertices
    list<int>*adj; // Pointer to an array containing adjacency lists

    public :
        Graph(int V);// Constructor
        void addEdge(int v, int w); // Function to add an edge to graph
        void BFSVisit(int s); // BFS traversal of the vertices reachable from s
};

Graph::Graph(int V){
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w); // Add w to v's list
    adj[w].push_back(v); // Add v to w's list
}

//BFS traversal of the vertices reachable from s
void Graph::BFSVisit(int s){
    //Mark all the vertices as not visited
    bool *visited = new bool[V];
    for(int i = 0; i < V; i++)
        visited[i] = false;
    //Create a queue for BFS
    list<int>queue;
    //Mark the current node as visited and enqueue it
    visited[s] = true;
    queue.push_back(s);
    //'i' will be used to get all adjacent vertices of a vertex u
    list<int>::iterator i;
    int u;

    while(!queue.empty()){
        //Dequeue a vertex from queue and print it
        u = queue.front();
        cout << u << endl;
        queue.pop_front();
        //Get all adjacent vertices of the dequeued vertex u. if a adjacent has not been visited,
        //then mark it visited and enqueue it 
        for(i = adj[u].begin(); i != adj[u].end(); ++i)
            if(!visited[*i]){
                visited[*i] = true;
                queue.push_back(*i);
            }
    }
}

int main(){
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    cout << "Following is Depth First Traversal (starting from vertex 0) \n";
    g.BFSVisit(0);
    return 0;
}