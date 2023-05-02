#include <stdio.h>

void saludador();
int selector;

int main(){
    printf("Iniciar el programa?    SI=1 / NO=0");
    scanf("%d", &selector);

    if(selector>0){
        saludador();
    }

    return 0;
}

void saludador (){
    char nombre[] = "jeje";
    printf("hola puto, como te llamas?");
    scanf("%s", &nombre);
    printf("aiii hola %s, boludooo", nombre);
}
