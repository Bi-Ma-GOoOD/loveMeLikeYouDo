/*Adjacency list ที่ถูกเขียนด้วย c++ โดยใช้ library vectore นี้จะทำงานได้ดีกว่า 
Adjacency Matrix มากๆ เรามาดูกัน*/

#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

vector<int>*createGraph(int n){
    return new vector<int>[n];
}
void addEdge(vector<int>*adjList, int u, int v){
    adjList[u].push_back(v);
}
void printGraph(vector<int>*adjList, int vertices){
    for(int v = 0; v < vertices; ++v){
        printf("[ %d ] head", v);
        for(int i = 0; i < adjList[v].size(); ++i){
            printf(" ->%d", adjList[v].at(i));
        }
        printf("\n");
    }
    printf("\n");
}

int main(){
    int n = 5;

    vector<int>*adjList = createGraph(n);

    addEdge(adjList, 0, 2);
    addEdge(adjList, 0, 4);
    addEdge(adjList, 4, 1);
    addEdge(adjList, 4, 3);
    addEdge(adjList, 2, 1);

    printGraph(adjList, n);
    return 0;
}