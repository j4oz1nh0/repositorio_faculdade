#include <stdio.h>
#include <stdlib.h>
float potencia (float a, int b){
    float mult=1.0;
    for (int i=b; i>0; i--){
        mult = mult * a;
    }
    return mult;
}
int main(){
    float a;
    int b;
    scanf("%f", &a);
    scanf("%d", &b);
    float r = potencia(a, b);
    printf("%.2f\n", r);
    return 0;
}