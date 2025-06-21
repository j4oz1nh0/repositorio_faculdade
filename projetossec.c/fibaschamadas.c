#include <stdio.h>
#include <stdlib.h>
int fib(int valor, int *calls){
    (*calls)++;
    if (valor==0){
        return 0;
    }
    else if(valor==1){
        return 1;
    }
    else{
        return fib(valor-1, calls)+fib(valor-2, calls);
    }
}
int main(){
    int vezes;
    scanf("%d", &vezes);
    for (int i= 0; i<vezes; i++){
        int calls = -1;
        int valor;
        scanf("%d", &valor);
        int r = fib(valor, &calls);
        printf("fib(%d) = %d calls = %d\n", valor, calls, r);
    }
}