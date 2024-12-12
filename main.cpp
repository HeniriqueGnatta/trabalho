#include <iostream>
using namespace std;

int main() {
  string nome;  // Variável para armazenar o nome
  cout << "Qual é o seu nome? "; // Pergunta o nome do usuário
  cin >> nome;

    
  for (int i = 0; i < 100; i++) { // Repete o nome 10 vezes
    cout << nome << endl;  // Imprime o nome
    }

    return 0;  // Indica que o programa terminou 
}
