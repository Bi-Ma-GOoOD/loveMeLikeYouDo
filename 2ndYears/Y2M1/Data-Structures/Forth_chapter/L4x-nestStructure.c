#include <stdio.h>
#include <string.h>

int main(){
    struct address{
        char district[20];
        char city[20];
    };
    struct student{
        char name[20];
        int age;
        struct address st_addr;
    };
    struct student st;
    strcpy(st.name, "Alice");
    st.age = 20;
    strcpy(st.st_addr.district, "Muang");
    strcpy(st.st_addr.city, "Bankok");

    printf("Name: %s\n",st.name);
    printf("Age: %d\n",st.age);
    printf("Address District: %s in City: %s\n",st.st_addr.district,st.st_addr.city);
    return 0;
}