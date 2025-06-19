#include <stdio.h>
int main(){
    int a;
    scanf("%d", &a);
    int v[a];
    for (int i=0; i<a; i++){
        v[i]=i+1;
    }
    for (int b; b<a-1; b++){
        int temp;
        scanf("%d", &temp);
        for (int c=0; c<a; c++){
            if (temp==v[c]){
                v[c]=0;
            }
        }
    }
    for (int d=0; d<a; d++){
        if (v[d]>0){
            printf("%d\n", v[d]);
        }
    }
    return 0;
}