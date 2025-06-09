#include <stdio.h>
#include <stdlib.h>
int main(){
    int v[20];
    int maior = 0;
    int ind = 0;
    for (int i=0; i<20; i++){
        scanf("%d", &v[i]);
        if (v[i]>maior){
            maior = v[i];
            ind = i;
        }
    }
    printf("%d\n%d", maior, ind);
    return 0;
}