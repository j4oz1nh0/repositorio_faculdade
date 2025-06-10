#include <stdio.h>
int palavra(char v[]){
    int tam=0;
    printf("%s\n", v);
    while (v[tam] !='\0'){
        tam++;
    }
    return tam;
}