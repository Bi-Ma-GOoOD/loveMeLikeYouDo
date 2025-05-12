#include <iostream>
using namespace std;

int main(){
    int n = 10;
    // cin >> n;
    
    // input
    int ar[11] = {69, 82, 71, 64, 99, 78, 40, 56, 96, 88};
    // for(int i =0; i < n; i++){
    //     cin >> ar[i];
    // }
    //sort algorithm 
    int cur;
    int j;
    for(int i = 1; i < n; i++){
        cur = ar[i];
        j = i -1;
        while(ar[j] >cur && j>= 0 ){
            ar[j+1] = ar[j];
            j--;
        }
        ar[j+1] = cur;
    } 
    //printing
    for(int i = 0; i < n; i++){
        cout << ar[i] << " ";
    }
}