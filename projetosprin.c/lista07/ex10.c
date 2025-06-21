#include <stdio.h>
#include <stdlib.h>
int main(){
    int x;
    scanf("%d", &x);
    int* v = (int*) malloc(x*sizeof(int));
    for(int i = 0; i<x; i++){
        *(v+i)= 0;
        printf("%d ", *(v+i));
    }
}