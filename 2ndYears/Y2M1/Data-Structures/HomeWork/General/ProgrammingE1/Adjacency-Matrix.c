#include <stdio.h>
#include <stdlib.h>

// ก่อนที่เราจะสร้าง graph ได้ เราจำเป็นต้องรู้ Node ก่อน
int **createGraph(const int n);
// สร้างเส้นเชื่อมระหว่าง Node
void addEdge(int **adjMatrix, int u, int v);
void printGraph(int **adjMatrix, int n);

int main(){
    int n = 5;

    // create graph จะสร้าง อาเรย์ สองมิติขึ้นมา ต่อจากนั้นจะถูกเก็บไว้ในค่า **adjMatrix
    int **adjMatrix =  createGraph(n);  

    // ขั้นตอนนี้จะเป็นการโยงเส้นหรือว่า เชื่อมเส้นระหว่าง Node นั่นเอง
    printf("0 1 2 3 4 \n");
    printf("-------------\n");
    addEdge(adjMatrix, 0, 1);
    addEdge(adjMatrix, 0, 3);
    addEdge(adjMatrix, 1, 2);
    addEdge(adjMatrix, 1, 4);
    addEdge(adjMatrix, 2, 1);
    addEdge(adjMatrix, 2, 4);
    addEdge(adjMatrix, 4, 3);

    printGraph(adjMatrix, n);
    return 0;
}

int **createGraph(const int n){
    int **adjMatrix = malloc(sizeof(int*)*n);
    for(int i = 0; i < n; i++){
        // สร้างตัวแรกของแถวโดยใช้ malloc
        adjMatrix[i] = malloc(sizeof(int)*n);
        for(int j = 0; j < n; j++){
            // เติมเลขศูนย์ไปก่อน เติมเลขในแถวให้เต็มโดยใช้ ศูนย์ไปก่อน
            adjMatrix[i][j] = 0;
        }
    }
    return adjMatrix;
}

void addEdge(int **adjMatrix, int u, int v){
    adjMatrix[u][v] = 1;
}

void printGraph(int **adjMatrix, int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            printf("%d ", adjMatrix[i][j]);
        }
        printf("| %d", i);
        printf("\n");
    }
}