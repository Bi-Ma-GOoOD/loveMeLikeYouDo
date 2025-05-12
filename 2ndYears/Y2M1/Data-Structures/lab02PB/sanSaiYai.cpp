/* #include <iostream>
using namespace std;

typedef struct StoreNum{
    int data = 0;
}Store;

int main(){
    int amount, left, right;
    int max = -1;

    cin >> amount;
    Store *array[amount] = {NULL};

    for(int i = 0; i < amount; i++){
        cin >> left >> right;

        if(array[i] == NULL){
            Store *create = new Store();
            create->data = 1;
            array[i] = create;
        }
        if(left != 0 && array[left-1] != array[i]){
            array[left-1] = array[i];
            array[i]->data++;
        }
        if(right != 0 && array[right-1] != array[i]){
            array[right-1] = array[i];
            array[i]->data++;
        }
        if(array[i] -> data > max) max = array[i] -> data;
    }
    cout << max;
}*/