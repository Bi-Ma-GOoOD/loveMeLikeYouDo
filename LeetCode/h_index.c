#include <stdio.h>
#include <stdlib.h>
int hIndex(int *citations, int citationsSize);


int main() {
    int citations[3] = {1, 3, 1};
    int arraySize = sizeof(citations) / sizeof(citations[0]);
    int result = hIndex(citations, arraySize);
    // printf("\n");
    // printf("H_Index is: %d\n", result);
    printf("%d", result);
    return 0;
}
int hIndex(int *citations, int citationsSize){
    int i;
    // จอง อาเรย์สำหรับการเก็บจำนวนงานวิจัยที่มีการอ้างอิง เช่น 3 อ้างอิง มี 1 งานวิจัย
    int *paper_lists = (int *)calloc(sizeof(int), (citationsSize + 1)); 

    // 3 0 6 1 5
    // 0 0 0 0 0 0
    for(i = 0; i < citationsSize; i++){
        if(citations[i] > citationsSize) paper_lists[citationsSize] += 1;
        else paper_lists[citations[i]] += 1;
    }

    int h_index;
    int total = 0;

    for(i = citationsSize; i < (citationsSize + 1); i--){
        // printf("total = %d + %d\n", total, paper_lists[i]);
        total = total + paper_lists[i];
        // printf("Compared \ntotal: %d\nindex: %d\n", total, i);
        if(total >= i){
            h_index = i;
            break;
        }
    }
    free(paper_lists);
    return h_index;
}