#include <stdio.h>
int tempomin(int hor1, int min1, int hor2, int min2){
    int hortot = 0;
    int mintot = 0;
    if (hor1>hor2){
        hortot = 24 - (hor1-hor2);
    }
    else {
        hortot = hor2-hor1;
    }
    if (min2>min1){
        mintot=min2-min1;
    }
    else {
        mintot= 60 -(min1-min2);
    }
    hortot = hortot*60;
    mintot = mintot+hortot;
    return mintot;
}
int main(){
    int r = tempomin(10, 50, 10, 20);
    printf("%d", r);
};