#include <stdio.h>
#include <stdlib.h>
int main(){
    int num;
    scanf("%d", &num);
    int num0 = 0;
    int num1 = 1;
    for (int i=0; i<num; i++){
        int temp;
        if (i<(num-1)){
            printf("%d ", num0);
        }
        else{
            printf("%d", num0);
        }
        temp = num0 +num1;
        num0 = num1;
        num1 = temp;
        
    }
    return 0;
}