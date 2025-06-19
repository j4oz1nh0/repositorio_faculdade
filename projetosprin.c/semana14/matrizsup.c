#include <stdio.h>
int main(){
    double matriz [12][12];
    char sum;
    scanf(" %c", &sum);
    double num=0.0;
    for (int i = 0; i<12; i++){
        for (int j=0; j<12;j++){
            scanf("%lf", &matriz[i][j]);
        }
    }
    for (int i = 0; i<12; i++){
        for (int j=0; j<12; j++){
            if (i+j<11 && j>i){
                    num+=matriz[i][j];
                
            }
        }
    }
    if (sum=='S'){
        printf("%.1lf\n", num);
    }
    else if (sum=='M'){
        num = num/30;
        printf("%.1lf\n", num);
    }
    return 0;
}