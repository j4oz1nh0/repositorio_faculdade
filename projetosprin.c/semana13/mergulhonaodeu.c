#include <stdio.h>
int main(){
    int foi;
    int veio;
    int flag= 0;
    int vfoi[foi];
    for (int a=1; a<=foi; a++){
        vfoi[a-1]= a;
    }
    int vveio[veio];
    while (scanf(" %d %d", &foi, &veio) != EOF){
        for (int i=0; i<veio; i++){
            scanf("%d", &vveio[i]);
        }
        for (int b = 0; b<veio; b++){
            for (int c = 0; c<foi; c++){
                if (vveio[b]==vfoi[c]){
                    vfoi[c]=0;
                }
            }
        }
        for(int d=0; d<veio; d++){
            if (vveio[d]>0 && d==veio-1){
                printf("%d", vveio[d]);
            }
            else if (vveio[d]>0 && d<veio-1){
                 printf("%d \n", vveio[d]);
            }
            else{
                flag++;
            }
        }
        if (flag==veio){
            printf("*");
        }
    }

}