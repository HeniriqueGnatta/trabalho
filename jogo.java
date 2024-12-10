/*
* Autor: [Henrique Gnatta]
* Linguagem: [Java]
* Data: [10/12/2024]
* Descrição: [calculo de temperatura]
* Funcionalidades: []
* Versão: [1.0]
*/

import java.io.IOException;//iporta biblioteca
import java.util.Scanner;//iporta biblioteca


public class jogo {        //declara a class 
     public static void main(String[] args) throws IOException { //declara que main esta vazio e estatica
                
Scanner entra = new Scanner(System.in);//declaro que scanner agora e entra
System.out.println("digite qual a temperatura de sua cidade:");//pergunta um numero ausuario e armazena na variavel
double T = entra.nextDouble();//declaro que T e uma variavel do tipo double
System.out.println("1- Fahrenheit\n2-Kelvin");//printa qual medida de temperatura eu selecionar
int A = entra.nextInt();//armazen na variavel qual medida de temperatura escoli
switch (A) { //inicio o switch e coloco a variavel a para mostrar qual switch escoli
     case 1:// switch 1
          System.out.printf("A temperatura em  Fahrenheit é: %.2f",(T*1.8)+32); //printa a medida escolida e utilizo uma mascara no final e coloco a conta
          break; //para parar o switch
case 2: //switch 2
System.out.printf("A temperatura em Kelvin é: %.2f ",T+273.15); //printa a medida escolida e utilizo uma mascara no final e coloco a conta
     default: // e a ultima escolha se nenhuma das outros switch nao forem
          break;//para parar o switch
}
entra.close(); // termina que selecionei que scanner é entra
     }
}
