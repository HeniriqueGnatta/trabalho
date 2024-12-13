def Q():#define que tudo que estiver dentro de def sera a função
 
  
  import random
  A = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0  a 20
  g = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20 
  h = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20
  i = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20
  j = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20
  k = random.randint(0,20)#define que a variavel recebe valor da biblioteca de 0 a 20
  z = random.randint(1,11)#define que a variavel recebe valor da biblioteca de 0 a 10
  zz = random.randint(1,11)#define que a variavel recebe valor da biblioteca de 0 a 10
  zzz = random.randint(1,11)#define que a variavel recebe valor da biblioteca de 0 a 10
  
  vet = ["carinho de controle remoto","computador","notebook","celular","fone de ouvido","tv","video  game","desodorante","cadeira gamer","um berssa coin","uma pilha","uma caneta","enxada","mouse","teclado","ovo","chinelo","carregador","controle","massageador de pé","relogio inteligente","pacote office"]#criei um vetor para armazenar os itens
    
  print("Ola sua inteligencia sera testada ao maximo aproveite")#printa que sua aventura começara
  print("A cada resposta certa você ganhara um premio!!!")#printa que voce recebera um premio
  print("Quanto é %d x %d = "%(z,zz))#printa a conta com mascara
  B = int(input(""))#input pergunta qual o resultado e armazena na  variavel
  if(B == z*zz):#define que outro valor alem do resultado é errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[A])#mostra o premio pois puxa o premio do vetor
    z = random.randint(5,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zz = random.randint(5,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zzz = random.randint(5,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    print("Quanto é %d + %d x %d = "%(z,zz,zzz))#faz a conta ao usuario e utiliza mascara e variaveis para mudar o numero
    C = int(input("Digite o resultado: "))#pergunta o resultado
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return

  if(C == z + (zz * zzz)):#define que outro valor alem do resuktado está errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[g])#mostra o premio pois puxa o premio do vetor
    #input pergunta qual o resultado e armazena na variavel
    z = random.randint(6,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zz = random.randint(6,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zzz = random.randint(6,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    print("Quanto é %d + %d +%d = "%(z,zz,zzz))#printa a conta com mascara
    D = int(input("Digite o resultado: "))#pergunta o resultado
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return 
  if(D == z+zz+zzz):#define que outro valor alem de 360 est errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[h])#mostra o premio pois puxa o premio do vetor
  #input pergunta qual o resultado e armazena na variavel
    z = random.randint(7,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zz = random.randint(7,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zzz = random.randint(7,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    print("Quanto é %d * %d * %d = "%(z,zz,zzz))#printa a conta com mascara
    E = int(input("Digite o resultado: "))#pergunta o resultado
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return 
  if(E == z*zz*zzz):#define que outro valor alem do resultado está errado
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[k])#mostra o premio pois puxa o premio do vetor
   #input pergunta qual o resultado e armazena na variavel
    z = random.randint(8,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zz = random.randint(8,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    zzz = random.randint(8,11)#define que a variavel recebe valor da biblioteca de 0 a 10
    print("Quanto é %d x %d = "%(z,zz))#printa a conta com mascara
    F = int(input("Digite o resultado: "))#pergunta o resultado
  else:
    print("Infelizmente você perdeu :( Kkkkkkkk mó ruim 🤣🤣🤣🤣🤣")#printa como voce é ruim
    return 
  if(F == z*zz):#define que outro valor alem do resuktado está errado 
    print("Parabens Voce acertou")#printa que voce acertou 
    print("voce vai ganhar um premio")#printa que voce ira ganhar um premio
    print(vet[i])#mostra o premio pois puxa o premio do vetor
  else:
    print("Infelizmente voce perdeu:( kkkkkkkk mó ruim🤣🤣🤣🤣🤣")#printa que voce nao sabe matematica
          
  print("Obrigado por jogar 😎😎😎😎")#Faz um agradecimento por ter jogado
    
