#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int pot10 (int y){
    if (y==0){
        return 1;
    }
    else{
        return 10*pot10(y-1);
    }
}
int digitcount(int x){
       if (x == 0) return 1;
    int count = 0;
    while (x != 0) {
        x = x/10;
        count++;
    }
    return count;
}
void rec (int x, int valor, int* v){
    int temp = 0;
    int i = 0;
    while (valor>0){
        temp = pot10(valor-1);
        v[i] =(x/temp);
        x = x%temp;
        i++;
        valor--;
    }
}
bool ispalindrome(int x){
    if(x<0) return false;
    else if (x==0) return true;
    else{
    int valor = digitcount(x);
    int v[valor];
    rec(x, valor, v);
    int fim= (valor/2);
    for(int i = 0; i<fim; i++){
        if(v[i]!=v[valor-i-1]){
            return false;
        }
    }
    return true;
    }
}
int main(){
    int num;
    scanf("%d", &num);
    bool retorno = ispalindrome(num);
    if (retorno==true){
        printf("true\n");
    }
    else{
        printf("false\n");
    }
    return 0;
}