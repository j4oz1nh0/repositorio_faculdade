#include <stdio.h>
#include <stdlib.h>
void nomecerto(char* ptr, char leterr){
    for (int i= 0; ptr[i]!='\0'; i++){
        if (ptr[i]==leterr){
            ptr[i]=' ';
        }
    }

}
int main(){
    char nome[50];
    char leterr;
    scanf("%s", nome);
    getchar(); 
    scanf("%c", &leterr);
    nomecerto(nome, leterr);
    printf("%s", nome);
}