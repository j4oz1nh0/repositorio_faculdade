#include <stdio.h>
int main(){
    int l;
    int maior= -1;
    while (scanf("%d", &l) !=EOF){
        int v[l];
        for(int i=0; i<l; i++){
            scanf("%d", &v[i]);
            if (v[i]>maior){
                maior = v[i];
            }
        }
        if (maior<10){
            printf("1\n");
        }
        else if (maior>=10 && maior<20){
            printf("2\n");
        }
        else{
            printf("3\n");
        }
        maior = -1;
    }
    return 0;
}