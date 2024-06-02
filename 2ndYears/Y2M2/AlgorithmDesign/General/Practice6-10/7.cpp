#include <cstdio>
#include <algorithm>
using namespace std;
// sequence function that character connect
int findSequence(char *s){
    int current = 1;
    int maxLength = 1;

    for(int i = 0; s[i] != '\0'; i++){
        if(s[i] == s[i-1]){
            current ++;
        }else{
            current = 1;
        }

        if(current > maxLength){
            maxLength = current;
        }
    }
    return maxLength;
}

int main(){
    char s[20];
    int repeat;
    // input 
    scanf("%s", s);
    // find sequence that character connect
    repeat = findSequence(s);
    // output
    printf("Character connect %d words", repeat);
}