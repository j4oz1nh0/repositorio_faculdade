#include <stdio.h>
#include <stdlib.h>
void troca(float* a,float* b){
    float temp = *a;
    *a = *b;
    *b = temp;
}
int main(){
    float a = 1.02;
    float b = 1.03;
    troca(&a, &b);
    printf("%.2f %.2f",a, b);
    return 0;
}