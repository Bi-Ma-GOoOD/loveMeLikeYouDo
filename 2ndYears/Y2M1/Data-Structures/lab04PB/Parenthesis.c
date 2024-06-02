#include <stdio.h>

int main(){
    int countLeftParenthesis = 0;
    int countRightParenthesis = 0;
    int i = 0;
    char parenthesis[1000];

    scanf("%s", parenthesis);

    for(; parenthesis[i] != '\0'; i++){
        if(parenthesis[i] == '(') countLeftParenthesis++;
        else if(parenthesis[i] == ')')  countRightParenthesis++;
    }

    if((countLeftParenthesis == countRightParenthesis) && parenthesis[0] == '(' && parenthesis[i-1] == ')' ) printf("YES");
    else printf("NO");
}