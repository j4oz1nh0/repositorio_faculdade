#include <stdio.h>
#include <stdlib.h>
int main(){
    float * ptr;
    ptr = (float*) malloc(sizeof(float));
    *ptr = 3.14;
    float *c = ptr;
    printf("%.2f", *c);
    free(ptr);

}
