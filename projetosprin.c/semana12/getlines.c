#include <stdio.h>
#include <stdlib.h>

int main(){
    float soma= 0;
    int flag= 0;
    char nomi [100];
    float dist;
    while (scanf(" %[^\n] %lf", nomi, &dist) != EOF){
        soma+=dist;
        flag++;
    }
    printf("%.1lf\n", soma/flag);
    return 0;
}