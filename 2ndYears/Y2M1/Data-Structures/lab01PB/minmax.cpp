#include <iostream>
using namespace std;

int main(){
    int inp_num; // input number
    int ch_max = -99999; // check max number
    int ch_min = 99999; // check min number
    int temp_num; // temporary number input

    cin >> inp_num;

    for(int i = 0; i < inp_num; i++){
        cin >> temp_num;

        if(temp_num >= ch_max) {ch_max = temp_num;}
        if(temp_num <= ch_min) {ch_min = temp_num;}
    }
    cout << ch_min << endl;
    cout << ch_max << endl;
}