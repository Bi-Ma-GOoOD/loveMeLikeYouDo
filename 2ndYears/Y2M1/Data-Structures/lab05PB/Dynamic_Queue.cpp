#include <iostream>
#include <queue>
using namespace std;

int main(){
    queue<int>q;

    int round;
    int number;
    int condition;
    int count = 0;

    cin >> round;

    for(int i = 0; i < round; i++){
        cin >> condition; // 1 = push -> 2 = pop -> 3 = show first Queue -> 4 = show amount

        switch (condition){
            case 1:
                    cin >> number;
                    q.push(number);
                    count++;
                    break;
            case 2:
                    if(q.empty()){ // ถ้า ใน Q เรา Empty ก็ไม่ต้อง pop แล้วปล่อยไว้อย่างงั้น ไม่ต้องใช้ count
                        break;
                    }
                    else{
                        q.pop();
                        count--;
                        break;
                    }
            case 3:
                    if(count <= 0){
                        cout << "EMPTY" << endl;
                        continue;
                    }else{
                        cout << q.front() << endl;
                        break;
                    }
            case 4:
                    if(count <= 0) cout << "0" << endl;
                    else{
                        cout << count << endl;
                    }
        }
    }
}