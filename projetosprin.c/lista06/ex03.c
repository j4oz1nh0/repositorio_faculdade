#include <stdio.h>
#include <stdlib.h>
int main(){
    int mes;
    scanf("%d", &mes);
    switch (mes){
        case 1:
        printf("janeiro");
        break;
        case 2:
        printf("fevereiro");
        break;
        case 3:
        printf("marco");
        break;
        case 4:
        printf("abril");
        break;
        case 5:
        printf("maio");
        break;
        case 6:
        printf("junho");
        break;
        default:
        printf("mes invalido");
        break;
    }
    return 0;
}