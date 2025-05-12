#include <iostream>
using namespace std;

int main(){
    int channel ; // channel

    cin >> channel;

    int ary_ch[2001]; // store number
    int chk_line = 0; // check line 
    int max_num = -1; // maximum number
    for(int i = 0; i < channel; i++){
        cin >> ary_ch[i];
    }
    for(int i = 0; i < channel; i++){
        max_num = -1;
        for(int j = i+1; j < channel; j++){
            if(ary_ch[i] > max_num && ary_ch[j] > max_num){
                chk_line += 1;
                max_num = ary_ch[j];
            }
            else {continue;}
        }
    }
    cout << chk_line;
}