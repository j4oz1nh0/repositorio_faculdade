#include <stdio.h>
void funcao(int* x){
    *x = 11;
}
int main(){
    int x = 10;
    funcao(&x);
    printf("%d", x);
}