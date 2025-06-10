#include <stdio.h>
int main(){
    int n;
    int menor = 1001;
    int flag = -1;
    scanf("%d", &n);
    int x[n];
    for(int i=0; i<n; i++){
        scanf("%d", &x[i]);
        if (x[i]<menor){
            menor = x[i];
            flag = i;
        }

    }
    printf("Menor valor: %d\nPosicao: %d\n", menor, flag);
    return 0;
}