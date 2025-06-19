#include <stdio.h>
#include <stdlib.h>
int main(){
    int tamanho;
    scanf("%d", &tamanho);
    int num= 0 ;
    int matriz[tamanho][tamanho];
    int flag= 0;
    while(num<(tamanho*tamanho)){
        for (int b = flag; b<tamanho-flag; b++){
            num++;
            matriz[flag][b]=num;
        }
        for (int c = flag+1; c<tamanho-flag; c++){
            num++;
            matriz[c][tamanho-flag-1]=num;
        } 
        for(int d = (tamanho-2-flag); d>=flag; d--){
            num++;
            matriz[tamanho-flag-1][d]= num;
        }
        for(int e = (tamanho-2-flag); e>flag; e--){
            num++;
            matriz[e][flag]= num;
        }
        flag++;
    }
        for (int f= 0; f<tamanho;f++){
            for (int g= 0; g<tamanho; g++){
                printf("%4d  ", matriz[f][g]);
                }
            printf("\n");
        }

}