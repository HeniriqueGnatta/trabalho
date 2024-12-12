/*
* Autor: [Henrique Gnatta]
* Linguagem: [C]
* Data: 12/12/2024
* Descrição: [utilizei if e variaveis enoperadores]
* Funcionalidades: [é trasformar a temperatura de celsius em fahrenheitn e Kelvin]
* Versão: [1.0]
*/
#include <stdio.h>

int main() {
float T = 0;//declaro a variavel como T
int A=0;//declara a variavel A float
 printf("DIgite a Temperatura de sua cidade: ");//pergunta qual a tenperatura da sua cidade
  scanf("%f",&T);//armazena o valor digitado na variavel
  printf("1-Fahrenheit\n2-Kelvin\n");//printa se a pessoa quer Fahrenheit ou Kelvin
    scanf("%d",&A);//armazena o valor na variavel
  if(A==1){ // inicio o if se for == a A printar Fahrenheit
    printf("A Temperatura em Fahrenheit é: %.2f",T*1.8+32);}// printa a temperatura e uso uma mascara e faço a conta
  if(A==2){//// inicio o if se for == a A printar Kelvin
    printf("A Temperatura em Kelvin é: %.2f ",T+273.15);//printa a temperatura usa a mascara e executo a conta
  }
  return 0;//para quando o codigo terminae retornar 0
}
