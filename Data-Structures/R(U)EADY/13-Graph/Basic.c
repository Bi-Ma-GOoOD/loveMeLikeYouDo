/*Basic Operation on Graphs*/

//createGraph
//implementation of singly linked list
struct Node{
    int adj_vertex;
    struct Node *next;
};

//Create the graph using adjacent-matrix representation
int **createGraph(const int n){
    //return 2D array of size n*n
    int **adjMatrix = malloc(sizeof(int *)*n);
    for(int i = 0; i < n; i++){
        adjMatrix[i] = malloc(sizeof(int)*n);
        for(int j = 0; j<n; j++){
            adjMatrix[i][j] = 0;
        }
    }
    return adjMatrix;
}

//Add the edge to the graph using
//adj-matrix representation
void addEdge(int **adjMatrix, int u, int v){
    adjMatrix[u][v] = 1;
}

//Print the adjacency-matrix representation of the graph
void printGraph(int **adjMatrix, int  n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            printf("%d", adjMatrix[i][j]);
        }
        printf("\n");
    }
}

//Delete the adjacency-matrix representation of the graph
void deleteGraph(int **adjMatrix, int n){
    for(int i= 0; i < n; i++)
        free(adjMatrix[i]);
    free(adjMatrix);
}