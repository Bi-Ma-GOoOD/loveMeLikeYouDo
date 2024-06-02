#include <stdio.h>

int main(){
    char message[15] = "Hello student!";
    char  course[9] = {'0', '1', '4', '1', '8', '2', '3', '1', '\0'};
    char vocab[4] = {'a', 'n', 't', '\0'};
    printf("sentence 1: %s\n", message);
    printf("sentence 2: %s\n", course);
    printf("sentence 3: %s\n", vocab);
    return 0;
}