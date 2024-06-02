#include <iostream>
#include <queue>
using namespace std;

struct Person{
    int order; // ลำดับ คิว ของคนที่ต่อแถว
    int money; // เงินที่ต้องการจะถอน
};

int main(){
    /* เหตุผลที่เราต้องสร้าง struct เป็น pointer เพราะว่าจะช่วยใน
    บรรทัดที่ 22 เพราะว่า ถ้าหากค่านั้นออกจาก for loop เมื่อไรค่าก็หาย
    แต่ถ้าเป็น pointer ค่าก็จะไม่หายไป */
    queue<struct Person*>q;

    int peopleInQueue;
    int maxWithdraw;
    cin >> peopleInQueue >> maxWithdraw;

    for(int i = 0; i < peopleInQueue; i++){
        int receive;
        cin >> receive ;
        struct Person *p = new Person();
        p->order = i+1; // เก็บจำนวน คนต่อคิว
        p->money = receive; // เก็บจำนวนเงินสำหรับคนนั้น
        q.push(p); // push คนที่ต่อคิวคนนั้น
    }

    /* Loop จนกว่า ใน คิว จะ empty*/
    while(!q.empty()){
        /* ในบรรทัดที่ 31-33 จะเป็นการเข้าถึงเงินของคนๆนั้นและนำเงินมาคิดคำนวณกับค่า max ของเงินที่ถอนได้*/
        struct Person *p = q.front();
        q.pop();
        p->money = p->money-maxWithdraw; 
        /* ซึ่งถ้าหากว่า เงินยังมากกว่า 0 อยู่คือยังถอนได้ไม่ครบตามจำนวนที่ตัวเองต้องการา
        ก็จะเอาตัวนั้นไป  push และวนอีกรอบนึง
        แต่!!! ถ้าหากถอนเงินได้ครบตามจำนวนแล้ว ก็ print ออกได้เลย*/
        if(p->money > 0) q.push(p);
        else 
            cout << p->order << " ";
    }
}