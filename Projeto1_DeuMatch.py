### Formação Análise de Dados Resilia/Senac ###
###     Módulo 2 - Projeto 'Deu Match!'     ###
###             Cassio Ribeiro               ###

print("Seja bem vindo ao seletor de candidatos DEU MATCH !!")
print("-"*50)

import pandas as pd   #Importando a biblioteca pandas que será usada no código


seleçao = []          #lista vazia onde os dados dos candidatos serão guardados.

while True:
  nome = str.title(input("Digite o nome do candidato: "))   #Variável 'nome' que guardará o nome dos candidatos.
  print("-"*50)                                             #print para melhorar a visualização.
  e = int(input("Digite a avaliação da entrevista: "))      #Variável 'e' que guardará a avaliação da entrevista do candidato.
  print("-"*50)
  t = int(input("Digite a avaliação da teste teórico: "))   #Variável 't' que guardará a avaliação do teste teórico do candidato.
  print("-"*50)
  p = int(input("Digite a avaliação da teste prático: "))   #Variável 'e' que guardará a avaliação do teste prático do candidato.
  print("-"*50)
  s = int(input("Digite a avaliação da soft skills: "))     #Variável 'e' que guardará a avaliação d softs skills do candidato.
  print("-"*50)
  seleçao.append([nome,e,t,p,s,f"e{e}_t{t}_p{p}_s{s}"])     #Append responsável por criar uma nova lista dentro da lista seleçãoe ja cria o resultado formatado
  
  sair = str.upper(input("Deseja inserir dados de mais candidatos? [S/N] "))  #variável para sair ou contimuar do código.
  if sair == "N":     #condicionais para sair ou permanecer no loop
    break
  else:
    pass
  


def achar (lista):                   #def criada para achar o candidatos aptos conforme parametros passados pelo usuário.
    print("-"*50)
    a=int(input("Vamos começar a pesquisa. Por favor nos diga a nota da entrevista: "))   #\
    print("-"*50)                                                                          #\
    b = int(input("Agora do teste teórico: "))                                              #\
    print("-"*50)                                                                            #Variáveis onde o usuário insere os parâmetros para pesquisa de candidatos aprovados.
    c = int(input("E do teste prático? "))                                                  #/
    print("-"*50)                                                                          #/
    d = int(input("Finalmente a ultima, nos diga a nota do teste de soft skills: "))      #/
    print("-"*50)
    df = pd.DataFrame(lista)                       #transformação da lista indicada pelo usuário em um data frame.
    dff = df[(df[1] >= a) & (df[2] >= b) & (df[3] >= c) & (df[4] >= d)]   #frame criad onde pegamos do freme original somente os candidatos que passaram conforme parametros dados pelo usuáriodo código. 
    dff.columns = ["Candidato","e","t","p","s","Resultado"]                   #dando nome as colunas que antes eram numéricas.
    dff = dff.drop(["e","t","p","s"], 1)                              #deletando as colunas que continham as notas para deixar o frame final conforme solicitação do usuário.
    print("Os candidatos que atendem aos requisitos são :")           #print de apresentação do frame final com os candidatos aprovados.
    return (print(dff))                                                      #return do frame final com os aprovados.



achar(seleçao)               # linha final onde chamamos a função para retornar os candidatos aprovados conforme parâmetros passados.



