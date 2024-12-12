#include <stdio.h>

int main() {
float T = 0;//declaro a variavel como T
int A=0;//declara a variavel A float
 printf("DIgite a Temperatura de sua cidade: ");//pergunta qual a tenperatura da sua cidade
  scanf("%f",&T);//armazena o valor digitado na variavel
  printf("1-Fahrenheit\n2-Kelvin\n");//printa se a pessoa quer Fahrenheit ou Kelvin
    scanf("%d",&A);//armazena o valor na variavel
switch(A){ // inicio o switch case
  case 1: //case 1
    printf("A Temperatura em Fahrenheit é: %.2f",(T*1.8)+32);// printa a temperatura e uso uma mascara e faço a conta
  break;//para parar a case 1
  case 2://case 2
    printf("A Temperatura em Kelvin é: %.2f ",T+273.15);//printa a temperatura usa a mascara e executo a conta
break;}//determina que terminou o switch case
  return 0;//para quando o codigo terminae retornar 0
}