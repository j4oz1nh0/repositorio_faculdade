#include <stdio.h>
#include <stdlib.h>
int jogadado (int num_faces){
    int aleatorio = (rand()%num_faces)+1;
    return aleatorio;
}
int testa_dados (){
    int dado10 = 0;
    int dado50 = 0;
    int dado100 = 0;
    for (int i = 0; i<100; i++){
        int temp = 0;
        temp = jogadado(10);
        dado10 += temp;
    }
    for (int i = 0; i<50; i++){
        int temp = 0;
        temp = jogadado(20);
        dado50 += temp;
    }
    int temp = 0;
    temp = jogadado(100);
    dado100 += temp;

    if (dado10>dado50 && dado10>dado100){
    return 10;
    }
    if (dado50>dado10 && dado50>dado100){
    return 50;
    }
    if (dado100>dado50 && dado100>dado10){
    return 100;
    }
    else {
        return 0;
    }
}