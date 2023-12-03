#include <stdio.h>

main(){
    int a = 10, b = 20;
    int *p, *q;

    printf("a = %d\t b = %d\n", a, b);
    printf("address a = %p\t address b = %p\n\n", &a, &b);


    p = &a;
    printf("After assign p = &a;\n");
    printf("p point to address %p, value is %d\n", p, *p);
    printf("Conclude:pointer p points to variable a");
    printf(" ,so a = *p= %d\n\n", a);

    q = p;
    printf("After assign q = p;\n");
    printf("q point to address %p, value is %d\n", q, *q);
    printf("Conclude:assign address of p to q");
    printf("( q point to a same as p )\n");
    printf("So a = *p = *q = %d\n\n", a);

    q = &b;
    printf("After assign q = &b;\n");
    printf("q point to address %p, value is %d\n", q, *q);
    printf("Conclude:pointer q pint to variable b");
    printf(",so b = *q = %d\n\n", b);

    a = (int)p;
    printf("After assign a = p;\n");
    printf("Value of a will be change to %d(%p)\n\n", a, a);

    *p = *q;
    printf("After assign *p = *q;\n");
    printf("Value of *p will be change to %d\n\n", *p);

    *q = 30;
    printf("After assign *q = 30;\n");
    printf("Value of *q will be change to %d\n\n", *q);
    printf("a = %d\n", a);
    printf("b = %d\n", b);
    printf("*p = %d\n", *p);
    printf("*q = %d\n", *q);
}