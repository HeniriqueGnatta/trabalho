def Q():#define que tudo que estiver dentro de def sera a função
 
  
  import random
  A = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0  a 20
  g = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20 
  h = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20
  i = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20
  j = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20
  k = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20

  vet = ["carinho de controle remoto","computador","notebook","celular","fone de ouvido","tv","video game","desodorante","cadeira gamer","um berssa coin","uma pilha","uma caneta","enxada","mouse","teclado","ovo","chinelo","carregador","controle","massageador de pé","relogio inteligente","pacote office"]#criei um vetor para armazenar os itens
    
  print("Ola sua inteligencia sera testada ao maximo aproveite")#printa que sua aventura começara
  print("A cada resposta certa você ganhara um premio!!!")#printa que voce resebera um premio

  B = int(input("quanto é = 22 x 30= "))#input pergunta qual o resultado e armazena na  variavel
  
  if(B == 660):#define que outro valor alem de 660 est errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[A])#mostra o premio pois puxa o premio do vetor
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return
  C = int(input("quanto é 2+4*11= "))#input pergunta qual o resultado e armazena na variavel
  if(C == 46):#define que outro valor alem de 46 est errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[g])#mostra o premio pois puxa o premio do vetor
    D = int(input("quanto é 730/2= "))#input pergunta qual o resultado e armazena na variavel
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return 
  if(D == 360):#define que outro valor alem de 360 est errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[h])#mostra o premio pois puxa o premio do vetor
    E = int(input("quanto é 80/20= "))#input pergunta qual o resultado e armazena na variavel
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return 
  if(E ==4):#define que outro valor alem de 4 est errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[k])#mostra o premio pois puxa o premio do vetor
    F = int(input("quanto é 30*3= "))#input pergunta qual o resultado e armazena na variavel
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return 
  if(F==90):#define que outro valor alem de 90 est errado
      print("Parabens Voce acertou")#printa que voce acertou 
      print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
      print(vet[i])#mostra o premio pois puxa o premio do vetor
  else:
    print("Infelizmente voce perdeu:( kkkkkkkk mó ruim🤣🤣🤣🤣🤣")#printa que voce nao sabe matematica
          
  print("Obrigado por jogar 😎😎😎😎")#Faz um agradecimento por ter jogado
    