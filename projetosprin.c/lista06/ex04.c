#include <stdio.h>
#include <stdlib.h>
/*int main(){
    int n;
    scanf("%d", &n);
    int v[n];
    v[0]=1;
    for (int i=1; i<n; i++){
        if (i==1){
            v[i]=v[i-1]+3;
            
        }
        else if (v[i-1]!=v[i-2]){
            if (v[i-1]>v[i-2]){
                v[i]=v[i-1];
            }
            else{
                v[i]=v[i-1]+3;
            }
        }
        else if (v[i-1]==v[i-2]){
            v[i]=v[i-1]-2;
        }
    }
    for (int h = 0; h< n; h++) {
        printf("%d ", v[h]);
    }
    return 0;
}*/

int main(){
    int num;
    scanf("%d", &num);
    int i = 1;
    int l = 4;
    int h = 0;
    while (h<num){
        if (h%3==0){
            printf("%d", i);
            i++;
        }
        else{
            printf(" %d %d ", l, l);
            l++;
            h++;
        }
        h=h+1;
    }
}