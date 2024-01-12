#include <cstdio>
#include <algorithm>
// กำหนด ให้ n = 6
#define N 7
using namespace std;

int main(){
    char order[N], str[N];
    char temp[N], rersult[N];
    int i, j;
    int position = 0;
    // input order
    scanf("%s", order);
    // input str
    scanf("%s", str);
    // check
    for(i = 0; order[i] != '\0'; i++){
        for(j = 0; str[j] != '\0'; j++){
            if(str[j] == order[i]){
                temp[position] = str[j];
                str[j] = '0';
                position++;
            }
        }
    }
    // output
    for(i = 0; order[i] != '\0'; i++){
        printf("%c ", order[i]);
    }
}