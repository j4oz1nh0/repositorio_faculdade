#include <stdio.h>
int main(){
    int linha;
    int coluna;
    scanf("%d %d", &linha, &coluna);
    int matriz[linha][coluna];
    int count;
    int num=0;
    for (int i=0;i<linha;i++){
        int temp=-1;
        int numeros = 0;
        for (int j=0;j<coluna;j++){
            scanf("%d", &matriz[i][j]);
            while(numeros!=1){
                if (matriz[i][j]==0){
                    temp+=1;
                }   
                else{
                numeros+=1;
                } 
            }
            if (temp>count && numeros>0){
                count=temp;
            }
        if (matriz[i][j]==0){
                num+=1;
            }
            if (num=coluna){
            printf("S");
            break;
            }
            else{
            printf("N");
            break;    
        }
        } 
    }  
}
