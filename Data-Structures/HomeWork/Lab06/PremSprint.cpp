#include <cstdio>
#include <list>
using namespace std;

typedef struct Position{
    int x, y;
}position;

int main(){
    int space, i, j;
    list<Position*> *positions = new list<Position*>();
    // printf("Enter matrix space: ");
    scanf("%d", &space);

    int matrix[space][space];
    for(i = 0; i < space; ++i){
        for(j = 0; j < space; ++j){
            scanf("%d", &matrix[i][j]);
        }
    }
    position *at = new position();
    at->x = 0;
    at->y = 0;
    positions->push_back(at);
    matrix[0][0] = 2;

    while(!positions->empty()){
        position *pointxNy = positions->back();
        positions->pop_back();
        if((pointxNy->x-1 >= 0) && matrix[pointxNy->x-1][pointxNy->y] == 0){// x-1 ด้านบน
            matrix[pointxNy->x-1][pointxNy->y] = 2;
            position *newAt = new position();
            newAt->x = pointxNy->x-1;
            newAt->y = pointxNy->y;
            positions->push_back(newAt);
        }
        if((pointxNy->x+1 < space) && matrix[pointxNy->x+1][pointxNy->y] == 0){// x+1 ด้านล่าง
            matrix[pointxNy->x+1][pointxNy->y] = 2;
            position *newAt = new position();
            newAt->x = pointxNy->x+1;
            newAt->y = pointxNy->y;
            positions->push_back(newAt);
        }
        if((pointxNy->y-1 >= 0) && matrix[pointxNy->x][pointxNy->y-1] == 0){// y-1 ด้านซ้าย
            matrix[pointxNy->x][pointxNy->y-1] = 2;
            position *newAt = new position();
            newAt->x = pointxNy->x;
            newAt->y = pointxNy->y-1;
            positions->push_back(newAt);
        }
        if((pointxNy->y+1 < space) && matrix[pointxNy->x][pointxNy->y+1] == 0){// y+1 ด้านขวา
            matrix[pointxNy->x][pointxNy->y+1] = 2;
            position *newAt = new position();
            newAt->x = pointxNy->x;
            newAt->y = pointxNy->y+1;
            positions->push_back(newAt);
        }
    }

    if(matrix[space-1][space-1] == 2) {printf("YES");}
    else {printf("NO");}
}