#include <stdio.h>

int main(){
    int num, min, max, i;
    i = 0;
    min = 0;
    max= 0;

    do{
        printf("ingrese numero entero positivo. Para finalizar negativo");
        scanf("%d", &num);

        if(num<min){
            min=num;
        }

        if(num>max){
            max=num;
        }

        }while(num>0);

    printf("el max es %d y el min es %d",max,min);


    return 0;
}
