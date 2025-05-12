#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int>getStack;
    int count = 0; // count member stack
    int numStore; // number as you want to store in stack
    int condition; // condition 1.push 2.pop 3.show member top stack 4.show member amount
    int round; // round to loop
    int tempCount;

    cin >> round;

    for(int i = 0; i < round; ++i){
        cin >> condition;
        switch(condition){
            case 1:
                    cin >> numStore;
                    getStack.push(numStore);
                    count++;
                    break;
            case 2:
                    if(getStack.empty()){
                        break;
                    }
                    else{
                        getStack.pop();
                        count--;
                        break;
                    }
            case 3:
                    if(count <= 0){
                        cout << "EMPTY" << endl;
                        continue;
                    }
                    else{
                        cout << getStack.top() << endl;
                        break;
                    }
            case 4:
                    if(count <= 0) cout << 0;
                    else{
                        cout << count << endl;
                    }
        }
    }
}