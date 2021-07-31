#include<stdio.h>
#include<stdlib.h>
int somatorio(int n){
    int i = 0;
    int soma = 0;

    for(i = 0; i <= n; i++) {
        soma += i;
    }
    return soma;
}

int main(){
    printf("%d \n", somatorio(10));
    return 0;
}