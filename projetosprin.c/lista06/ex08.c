#include <stdio.h>
#include <stdlib.h>
int valormed(int v[], int tam){
    int media=0;
    for(int i=0; i<tam; i++){
        media = media+v[i];
    }
    media = media/tam;
    return media;
}
int main(){
    int tam = 0;
    scanf ("%d", &tam);
    int v[tam];
    for(int b=0; b<tam; b++){
        scanf("%d", &v[b]);
    }
    int r= valormed(v, tam);
    printf("%d", r);
}