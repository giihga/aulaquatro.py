#Desenvolva um programa Python que devolva leia um nome e uma data e retorne uma String. 
#Neste caso o programa vai falar a data de nascimento de alguém. Veja um exemplo:
#>> Digite o Nome: HENRIQUE >> Digite o mês: 01 >> Digite o ano: 1996
#>> Henrique nasceu no dia: 01/01/1996

#IMPORTANTE: Veja que o nome foi digitado em letras maiúsculas e a resposta foi dada só com a primeira letra
#maiúscula. Isso significa que não importa se a pessoa digitar letras maiúsculas ou minúsculas, 
#o nome sempre deverá ser mostrado apenas com a primeira letra maiúscula. 

#print(a.upper(A)
#print(a.lower(a)

nome = input('Digite seu nome? ')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')

data = nome + dia + mes + ano


print ('Ola  {} você nasceu no dia  {} de {} de {}'.format(nome.capitalize(), dia, mes, ano))