#include <stdio.h>
#include <string.h>

int main(){
    char data[20] = "xxxx-xxxx-xxxx-xxxx";
    printf("Before change\n");
    printf("data is %s\n\n", data);
    strcpy(data, "1234-5678-9999");
    printf("After change for first time\n");
    printf("data is %s\n\n", data);
    strcpy(data, "Hello :>");
    printf("After change for second time\n");
    printf("data is %s", data);
}