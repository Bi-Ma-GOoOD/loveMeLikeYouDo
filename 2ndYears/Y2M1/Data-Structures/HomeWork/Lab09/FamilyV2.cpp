#include <iostream>
#include <list>
#include <cstdio>
using namespace std;

class Graph{
    int v;
    list<int> *adj;

    void DFSVisit(int s, bool visited[]);

    public:
    Graph(int v);
    void addEdge(int v, int w);
    void DFSInit(int s);
};

Graph :: Graph(int v){
    this->v = v;
    adj = new list<int>[v];
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
    adj[w].push_back(v);
}

void Graph::DFSVisit(int s, bool visited[]){
    visited[s] = true;
    printf("%d", s);

    list<int>::iterator i;
    for(i = adj[s].begin(); i != adj[s].end(); ++i){
        if(!visited[*i]){
            DFSVisit(*i, visited);
        }
    }
}

void Graph::DFSInit(int s){
    bool *visited = new bool[v];
    for(int i = 0; i < v; i++){
        visited[i] = false;

    }
    DFSVisit(s, visited);
}

int main(){
    Graph g(5);
    g.addEdge(1,2);
    g.addEdge(1,3);
    g.addEdge(2,4);
    g.addEdge(3,5);
    printf("Start from vertex 3\n");
    g.DFSInit(3);
    return 0;
}