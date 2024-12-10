/*
* Autor: [Henrique Gnatta]
* Linguagem: [Java]
* Data: [10/12/2024]
* Descrição: [calculo de temperatura]
* Funcionalidades: []
* Versão: [1.0]
*/

import java.io.IOException;
import java.util.Scanner;


public class jogo {
     public static void main(String[] args) throws IOException {
                
Scanner entra = new Scanner(System.in);
System.out.println("digite qual a temperatura de sua cidade:");
double T = entra.nextDouble();
System.out.println("1- Fahrenheit\n2-Kelvin");
int A = entra.nextInt();
switch (A) {
     case 1:
          System.out.printf("A temperatura em  Fahrenheit é: %.2f",(T*1.8)+32);
          break;
case 2: 
System.out.printf("A temperatura em Kelvin é: %.2f ",T+273.15);
     default:
          break;
}
entra.close();
     }
}