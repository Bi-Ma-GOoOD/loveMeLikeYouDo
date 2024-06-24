#include <stdio.h>
//Conver fahrenheit to celcius
int convert(float *fahrenheit, float *celcius){
    *celcius = ((*fahrenheit-32)*5)/9;
    return 0;
}
//Driver code
int main(){
    //Declare variables
    float fahrenheit;
    float celcius;
    //Input fahrenheit
    printf("This code is use to convert Fahrenheit to Celcius\n");
    printf("Enter Fahrenheit : ");
    scanf("%f", &fahrenheit);
    //Call function convert
    convert(&fahrenheit, &celcius);
    //Output fahrenheit and celcius
    printf("Fahrenheit : %.1f\nCelcius : %.1f", fahrenheit, celcius);
}