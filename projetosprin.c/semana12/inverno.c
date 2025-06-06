#include <stdio.h>
int main(){
    int A;
    int B;
    int C;
    scanf("%d %d %d", &A, &B, &C);
if (A>B && C>=B){
    printf(":)\n");
    }
else if (B>A && B>=C){
    printf(":(\n");
    }
else if (A<B && B<C){
    if (C-B < B-A){
        printf(":(\n");
        }
    else{
        printf(":)\n");
        }
    }
else if (A>B && B>C){
    if (B-C < A-B){
        printf(":)\n");
        }
    else{
        printf(":(\n");
        }
    }
else if (A==B){
    if (C>B){
        printf(":)\n");
        }
    else{
        printf(":(\n");
        }
    }
}