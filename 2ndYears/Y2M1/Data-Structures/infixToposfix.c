/*  ⁡⁢⁢⁢⁡⁣⁣⁢Infix expression
    convert     to
    Postfix expression⁡⁡ */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_CHAR 100 // ⁡⁣⁢⁣บรรทัดนี้ต้องการจะสื่อว่า เราอยากจะกำหนดให้ Array ของเรามีขนาดเท่าไร่ 

void push(char);
char pop();
int isEmpty();
void intoPostfix();
int space(char);
void print();
int precedence(char);

char stack[100];
char infix[100], postfix[100];
int top = -1;

int main(){
    /* ⁡⁣⁢⁣รับสมการในรูปที่เป็น infix จากผู้ใช้งาน⁡ */
    printf("Enter the infix expression: ");
    gets(infix);

    /* ⁡⁣⁢⁣สร้างฟังก์ชันที่มีระบบการทำงานที่สามารถเปลี่ยน infix -> postfix ⁡*/
    intoPostfix();
    print();
    return 0;
}

void intoPostfix(){
    int i, j = 0;
    char symbol, next;// ⁡⁣⁢⁣สร้างตัวแปร symbol ขึ้นมาเพื่อเป็นการเก็บตัว สัญลักษณ์(operator) จากประโยค postfix⁡
    /* ⁡⁣⁢⁣เหตุผลที่มีการใช้ strlen เพราะว่า เราจะลุปตั้งแต่ตัวเลขไปจนถึงตัวก่อนหน้า '\0' นัั่นเอง
    โดย strlen จะค่นค่ามาเป็นจำนวนตัวเลขของ String นั้นๆ⁡ */
    for(i = 0;i < strlen(infix); i++){
        symbol = infix[i]; // ⁡⁣⁢⁣เราจะให้ค่า infix[i] = symbol แล้วเอา symbol ไปเช็ค⁡
        // ถ้า symbol ไม่ใช่ whitespace ช่องว่างอะงับ
        if(!space(symbol)){
            switch(symbol){
                case '(':
                        push(symbol);
                        break;
                case ')':
                /* ⁡⁣⁢⁡⁣⁢⁣ถ้าเจอวงเล็บปิดขวา เราจะทำการ Pop Stack[MAX] แล้วเอาตัวที่ pop อะเช็คว่า มีค่า precedence
                เ่ท่ากับ วงเล็บไหม วงเล็บมีค่าเป็น 0 อะต่ำสุดเลย⁡ ⁡*/
                        while((next=pop()) != '('){
                            postfix[j++] = next;
                        }
                        break;
                case '+':
                case '-':
                case '*':
                case '/':
                case '^':
                /* ⁡⁣⁢⁣เงื่อนไขการ check ข้างล่างนี้คือการนำ symbol ไปเช็คหาค่า ความสำคัญที่เราสร้างไว้ที่ 
                Function precedence⁡*/
                /* ⁡⁣⁢⁣isEmpty หมายถึงตัว Stack[MAX] ที่สร้างเลยอะ⁡ */
                        while(!isEmpty() && precedence(stack[top]) >= precedence(symbol)){
                            postfix[j++] = pop(); // ⁡⁣⁢⁣ถ้าหาสำคัญกว่า ก็ Pop operater ตัวล่าสุดออก⁡
                        }
                        push(symbol); //⁡⁣⁢⁣แล้วใส่ใหม่ แทนที่ที่ pop ไ⁡⁣⁢⁣ป หรืออีกอย่างนึงคือ เอาเข้ามาเหมือนกันถ้าไม่เข้า while⁡⁡
                        break;
                /*⁡⁣⁢⁣เมื่อไม่เจอ วงเล็บซ้ายและขวา หรือว่า ถ้าเอาตรงๆ ก็คือ ถ้าเจอตัวเลขอะ 
                ก็จะเข้า default ที่จะนำตัวเลขมาใส่ใน Postfix⁡*/
                default:
                        postfix[j++] = symbol; 
            }
        }
        /* ⁡⁢⁣⁡⁣⁢⁣เมื่อ Loop เสร็จแล้ว  Function มีหน้าที่แค่ทำการเติม '\0' เพื่อทำให้  Array นั้นจบลง⁡⁣⁢⁣
        ซึ่งแน่นอนว่า อะไรก็ตามที่ยังอยู่ใน Stack[MAX] ก็จะถูกนำมาเติมหลัง postfix ทั้งหมด และเติม '\0' จบท้าย⁡⁡*/
        }
        while(!isEmpty()){
            postfix[j++] = pop();
        }
        postfix[j] = '\0';
}
int space(char c){
    if(c == ' ' || c == '\t'){
        return 1;
    }else{
        return 0;
    }
}
/* ⁡⁢⁣⁣Function precedence นี้สร้างขึ้นมาเพื่อเป็นการเช็คความสำคัญของเครื่องหมาย ซึ่งความสำคัญในที่นี้เราให้เป็นค่าแทน ยิ่งสำคัญมาก
ค่าก็ยิ่งมีมากกว่า⁡ */
int precedence(char symbol){
    switch(symbol){
        case '^':
                return 3;
        case '/':
        case '*':
                return 2;
        case '+':
        case '-':
                return 1;
        default:
                return 0;
    }
}

void print(){
    int i = 0;
    printf("The equivalent postfix expression is: ");
    while(postfix[i]){
        printf("%c", postfix[i]);
        i++;
    }
    printf("\n");
}
void push (char c){
    if(top == MAX_CHAR -1){
        printf("Stack Overflow\n");
        return;
    }
    top++;
    stack[top] = c;
}
char pop(){
    char c;
    if(top == -1){
        printf("Stack Underflow\n");
        exit(1);
    }
    c = stack[top];
    top = top-1;
    return c;
}
int isEmpty(){
    if(top == -1)
        return 1;
    else
        return 0;
}