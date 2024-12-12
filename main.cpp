/*
* Autor: [Henrique Gnatta]
* Linguagem: [C++]
* Data: [12/12/2024]
* Descrição: [utilizei for e variaveis]
* Funcionalidades: [pergunta seu nome e pergunta um numero e repete seu nome quantas o numero colocado]
* Versão: [1.0]
*/
#include <iostream>
using namespace std;

int main() {
  string nome;//declara que a variavel e string 
  int carro;// declara que a variavel é int
  cout << "Qual é o seu nome? "; // Pergunta o nome do usuário
  cin >> nome;//aramazena valor recebido em nome    
  cout << "DIgite um numero ";//pergunta um numero
  cin >> carro;//armazena um valor digitado a carro

  for (int i = 0; i < carro; i++) { // Repete o nome 10 vezes
    cout << nome << endl;  // Imprime o nome
    }

    return 0;  // Indica que o programa terminou 
}
