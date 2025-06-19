#include <stdio.h>
int main(){
    int tam;
    while (scanf("%d", &tam) !=EOF){
        int matriz[tam][tam];
        for (int i = 0; i< tam; i++){
            for (int j = 0; j<tam; j++){
                matriz[i][j]=3;
                if (i==j){
                    matriz[i][j]= 1;
                }
                if (i+j==tam-1){
                    matriz[i][j]=2;
                }  
                printf("%d", matriz[i][j]);
            }
            printf("\n");
        }
    }
}