#include <iostream>
#include <vector>
using namespace std;

vector<int>* createGraph(int n);
void addEdge(vector<int>* graph, int connect, int connected);
int inDegree(vector<int>* graph, const int amountNode, int inDegreeAtNode);
int outDegree(vector<int>* graph, int outDegreeAtNode);

int main(){
    int amountNode, amountEdge, degreeIn, degreeOut, degreeAtPoint;

    // printf("enter node & edge: ");
    scanf("%d %d",&amountNode, &amountEdge);

    // printf("enter node that you want to know How many degrees? ");
    scanf("%d", &degreeAtPoint);

    vector<int>* graph = createGraph(amountNode);

    for(int i = 0; i < amountEdge; ++i){
        int node1, node2;
        // printf("Enter addEdge: ");
        scanf("%d %d",&node1, &node2);
        addEdge(graph, node1, node2);
    }
    degreeIn = inDegree(graph, amountNode, degreeAtPoint);
    degreeOut = outDegree(graph, degreeAtPoint);
    // printf("node[%d] have %d degrees.", degreeAtPoint, (degreeIn + degreeOut)); 
    printf("%d",degreeIn + degreeOut);    

}

vector<int>* createGraph(int n){
    return new vector<int>[n];
}
void addEdge(vector<int>* graph, int connect, int connected){
    graph[connect].push_back(connected);
}
int inDegree(vector<int>* graph, const int amountNode, int inDegreeAtNode){
    int count = 0, i , j;
    for(i = 0; i < amountNode; ++i){
        for(j = 0; j < graph[i].size(); ++j){
            if(graph[i].at(j) == inDegreeAtNode){ count ++;}
        }
    }
    return count;
}
int outDegree(vector<int>* graph, int outDegreeAtNode){
    return graph[outDegreeAtNode].size();
}