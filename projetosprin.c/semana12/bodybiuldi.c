#include <stdio.h>
int main(){
    float final=0.0;
    float contador=0.0;
    float conta1;
    float conta2;
    float media_conta;
while (1){
    float w1, w2, r;
    scanf("%f %f %f", &w1, &w2, &r);
    if (w1==w2 && w2==r && r==0){
        break;
    }
    conta1 = (w1*(1+(r/30)));
    conta2 = (w2*(1+(r/30)));
    media_conta =(conta1+conta2)/2;
    final+= media_conta;
    contador+=1.0;
    if (1<=media_conta && media_conta<13){
       printf("Nao vai da nao\n");
    }
    else if (13<=media_conta && media_conta<14){
        printf("E 13\n");
    }
    else if (14<=media_conta && media_conta<40){
       printf("Bora, hora do show! BIIR!\n");
    }
    else if (40<=media_conta && media_conta<=60){
        printf("Ta saindo da jaula o monstro!\n");
    }
    else if (media_conta>60){
        printf("AQUI E BODYBUILDER!!\n");
    }
}
    final=final/contador;
    if (final>40){
    printf("\n");
    printf("Aqui nois constroi fibra rapaz! Nao e agua com musculo!\n");
    }
    return 0;
}