#include <stdio.h>

int main(){
    int map[0][3] = {1, 4, 2, 5};
    int map[1][3] = {0, 4, 6, 5};

    for(int i = 0; i < 2; i++){
        printf("%d\n", map[i][3]);
    }
}