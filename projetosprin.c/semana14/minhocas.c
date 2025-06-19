#include <stdio.h>
int main (){
    int linha;
    int coluna;
    scanf("%d %d", &linha, &coluna);
    int matriz[linha][coluna];
    int maior = 0;
    for (int i = 0; i< linha; i++){
        int sumlinha = 0;
        for (int j = 0; j<coluna; j++){
            scanf("%d", &matriz[i][j]);
            sumlinha += matriz[i][j];
        }
        if (sumlinha> maior){
            maior = sumlinha;
            
        }
    }
    for (int i = 0; i< coluna; i++){
        int sumcoluna=0;
        for (int j = 0; j<linha; j++){
            sumcoluna += matriz[j][i];
        }
        if (sumcoluna> maior){
            maior = sumcoluna;
        }
    }
    printf("%d\n", maior);
    return 0;
}