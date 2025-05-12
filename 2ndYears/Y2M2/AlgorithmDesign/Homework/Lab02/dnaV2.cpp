// ทำไมไม่ผ่าน งง
#include <cstdio>
#define MAX 1000000
using namespace std;

int main(){
    char transcript[MAX];
    int i, max_length = 1, current_length = 1;
    // input
    // printf("Enter DNA Trascription : ");
    fgets(transcript, MAX, stdin);
    // find value i transcription
    for (i = 1; transcript[i] != '\0'; i++) {
        if (transcript[i] == transcript[i - 1]) {
            current_length++;
        } else {
            current_length = 1;
        }
        if (current_length > max_length) {
            max_length = current_length;
        }
    }
    // answer
    printf("%d\n", max_length);
}