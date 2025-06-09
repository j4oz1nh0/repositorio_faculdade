#include <stdio.h>
#include <stdlib.h>
int main(){
    int v [50];
    int soma= 0;
    for (int i=0; i<50; i++){
        v[i]=i+1;
        soma+=i;
        if (i<49){
            printf("%d ", v[i]);
        }
        else{
            printf("%d\n", v[i]);
        }
        
    }
    printf("%d", soma);
    return 0;
}