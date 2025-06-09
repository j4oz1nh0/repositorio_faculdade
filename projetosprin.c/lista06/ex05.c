#include <stdio.h>
#include <stdlib.h>
int main(){
    int matrix [10][10];
    for (int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            matrix [i][j]= i*j;
        }
    }
    for (int i=0; i<10; i++){
        for (int j=0; j<10; j++){
            if (j==9){
                printf("%4d\n", matrix[i][j]);
            }
            else{
                printf("%4d", matrix[i][j]);
            }
        }
    }
    return 0;
}