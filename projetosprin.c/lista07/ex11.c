#include <stdio.h>
#include <stdlib.h>
int somatorio (int* v){
    int soma=0;
    for(int i = 0; i<10; i++){
        soma+= v[i];
    }
    return soma;
}
int main(){
    int v[10];
    for(int i=0; i<10; i++){
        int *temp= (int*) malloc(sizeof(int));
        scanf("%d", temp);
        v[i]= *temp;
        free(temp);
        
    }
    for(int i=0; i<10; i++){
        printf("%d ", v[i]);
    }
    printf("\n");
    int r = somatorio(v);
    printf("%d", r);
    return 0;
}