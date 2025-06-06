#include <stdio.h>
#include <stdlib.h>
int main (){
    float sal;
    float B;
    float C;
    float D;
    scanf("%f", &sal);
    if (sal<2000.0){
        printf("Isento\n");
    }
    else if (sal> 2000.00 && sal<=3000.00){
        sal= sal-2000.00;
        B = sal*0.08;
        printf("R$ %.2f\n", B);
    }
    else if (sal>3000.00 && sal<=4500.00){
    sal = sal - 2000.00;
    B = 1000.00;
    C = sal- B;
    B = B*0.08;
    C = C*0.18;
    C = B+C;
    printf("R$ %.2f\n", C);
    }
    else if (sal>4500.00){
    sal = sal - 2000.00;
    B = 1000.00;
    C = 1500.00;
    D = sal - B - C;
    B = B * 0.08;
    C = C * 0.18;
    D = D * 0.28;
    D = B+C+D;
    printf("R$ %.2f\n", D);
    }
    return 0;
}