#include <stdio.h>
int main(){
    int vpar[5] = {0, 0, 0, 0, 0};
    int vimp[5] = {0, 0, 0, 0, 0};
    int flagpar = 0;
    int flagimp = 0;
    for (int i=0; i<15; i++){
        int num;
        scanf("%d", &num);
        if (num%2==0){
            if (flagpar<=4){
                vpar[flagpar] = num;
                flagpar++;
            }
            if (flagpar>=5){
                for(int a= 0; a<=4; a++){
                    printf("par[%d] = %d\n", a, vpar[a]);
                    vpar[a]=0;
                    flagpar=0;
                }
            }
        }
        else{
            if (flagimp<=4){
                vimp[flagimp] = num;
                flagimp++;
            }
            if (flagimp>=5){
                for(int b= 0; b<=4; b++){
                    printf("impar[%d] = %d\n", b, vimp[b]);
                    vimp[b]=0;
                    flagimp=0;
                }
            }
        }
    }
    for (int c= 0; c<=4; c++){
        if (vimp[c]!=0){
            printf("impar[%d] = %d\n", c, vimp[c]);
        }
    }
    for (int d=0; d<=4; d++){
        if (vpar[d]!=0){
            printf("par[%d] = %d\n", d, vpar[d]);
        }
    }
}