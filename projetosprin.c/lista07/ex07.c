#include <stdio.h>
#include <stdlib.h>
int main(){
    int *ptr;
    ptr = (int*) malloc(10*sizeof(int));
    for(int h=0; h<10; h++){
        *(ptr+h)=h;
    }
    for(int i=0; i<10; i++){
        printf("%d ", *(ptr+i));
    }

}