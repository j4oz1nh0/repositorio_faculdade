#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
void troca(float pipi, float* pipi2, float* pipi3){
    *pipi2 = pipi*pipi;
    *pipi3 = sqrt(pipi);
}
int main(){
    float pipi = 9.0;
    float pipi2 = 0;
    float pipi3= 0;
    troca(pipi, &pipi2, &pipi3);
    printf("%.1f %.1f", pipi2, pipi3);
}