#include <stdio.h>
#include <stdlib.h>
int main (){
    int v[25];
    for (int h=0; h<25; h++){
        int x;
        scanf("%d", &x);
        v[h]=x;
    }
    for (int i=0; i<12; i++){
        int temp = v[i];
        v[i]= v[24-i];
        v[24-i]=temp;
    }
    return 0;
}