/*Basic Operation on Adjacency List Graph*/

//create Graph by STL
#include <iostream>
#include <vector>
using namespace std;
#define NMAX 500

//Function to create a graph with n vertices
vector<int>*CreateGraph(){
    return new vector<int>[NMAX];
}

//Function to add a directed edge into the graph
void addEdge(vector<int>*adjList, int u, int v){
    adjList[u].push_back(v);
}

//Function to print the adjacency list representation of graph
void printGraph(vector<int>*adjList, int number){
    for(int v = 0; v < number; ++v){
        cout << "[" << v << "] head";
        for(int i = 0; i < adjList[v].size(); ++i)
            cout << "->" << adjList[v].at(i);
        cout << endl;
    }
    cout << endl;
}