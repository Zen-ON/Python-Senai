


""" hello = print('buenos dias')
#testando comentario """ 



""" print ('Somar 2 com 2', 2+2)
print ('Concatenar 2 com 2 ','2'+'2')
print ('Subtrair 2 com 2',2-2)
print ('Multiplicar 2 com 2',2*2)
print ('repete PY duas vezes','PY'*2)
print ('Dividir 10 com 2',10*2)
print ('inteiro de 10 com 2:',3%2)
print ('2 elevado a 3:',2**3)
 """

#Condicionais 
""" n1 = 7
n2 = 7
print (n1 == n2)
print (n1 >= n2)
print (n1 > n2)
print (n1 <= n2)
print (n1 < n2)
print (n1 != n2) """

#
""" n1 = 5
n2 = 5

nome = 'Orrico'
print (n1 == n2 and n1 >= n2)
print (n1 != n2 or n1 >= n2 )
print (not n1 == n2)
print ('rr' in nome )
print ('rr' not in nome ) """

#variaveis
""" nome = 'Orrico'
idade = 41
altura = 1.87
teste = True
print (type(nome))
print (type(idade))
print (type(altura))
print (type(teste))
 """
 #outros
""" nome= 'Orrico'
idade = 41
altura = 1.87
teste = True
print('O nome digitado foi', nome)
print ('{} tem {} anos!!!'.format(nome, idade)) """

#outros
""" nome= 'Orrico'
idade = 41
altura = 1.87
teste = True
print('O nome digitado foi', nome)
print ('{n} tem {i} anos!!!'.format(n=nome, i=idade)) """

""" nome = 'Orrico'
idade = 41
altura = 1.87
teste = True
print (f'{nome} tem {idade} anos !!!') """

""" nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
if idade >= '18':
    print('Pode tirar a CNH!!')
else:
    print('nada disso')    """  

""" nome = input('Digite o nome do usuario ')
salario = int(input('Digite seu salario: R$'))
print(f'O salario do(a) {nome} é de R${salario}')
if salario >= 1000:
    print(f'O(A) {nome} ganha bem!!!')
else:
    print(f'O(A) {nome}ganha pouco') """

""" sexo = input ('Digite a letra correspondente ao sexo:')
if sexo == 'm' or sexo == 'f':
    print('Sexo validado')
else:
    print('Sexo invalido')     """

""" nome = input('Digite seu nome:')
n1 = int(input('Digite a primeira nota'))
n2 = int(input('Digite a segunda nota'))
n3 = int(input('Digite a terceira nota'))
n4 = int(input('Digite a quarta nota'))  
m = int(n1+n2+n3+n4)/4
if m >= 7:
    print(f'(nome) sua media é {m} e voce foi aprovado')
elif m < 5:
    print(f'(nome) sua media é {m} e voce foi reprovado')
else:
    print(f'(nome) sua media é {m} e voce esta de recuperação')   """ 

""" print('Entre com o nome d eum time de futebol:')
time = input()
match time:
  case 'flamengo' | 'fluminense' |'vasco':
    print('É um time carioca')
  case 'sao paulo' | 'palmeiras' | 'corinthians':
    print('é de outro estado') 
  case _:
    print('é de outro estado') """

""" valor = float(input('Digite o valor da mercadoria: '))
op = int(input('Digite 1 para parcelar ou 2 para pagamento a vista:'))
match op:
  case 1:
   if valor > 1000:
    parcelas = valor/5
    print(f'Com esse valor voce pode parcelar em 5x de R$:{parcelas}')
   else:
    parcelas = valor/3
    print(f'Com esse valor voce pode parcelar em 3x de R${parcelas}')
  case 2:
    avista = (valor * 0.9)
    print(f'O valor a vista é :{avista}')
  case _:
    print ('Opção invalida')  """  
""" 
print('----------------------------------------------------')    
print('------        CRIANÇA ESPERANÇA             --------')      
print('----------------------------------------------------')
print('------------ muito obrigado por ajudar-----------')    
print('-[1] Para doar R$ 10,00                            -')      
print('-[2] Para doar R$ 25,00-----------------------------')
print('-[3] Para doar R$ 50,00-----------------------------')    
print('-[4] Para doar outros valores-----------------------')      
print('-[5] Para cancelar  --------------------------------')
d = int(input())
match d:
    case 1:
        valor = 10
    case 2:
        valor = 25
    case 3:
        valor = 50
    case 4:
        valor = int(input('Qual o valor da doação?'))
    case 5:
        print('Que pena, mas agradecemos mesmo assim!!!') 
print('------------------------------------------------------')                       
print(   f'Sua doação foi de R${valor}'                       )  
print('------   Muito  Obrigado                     ---------')
print('------------------------------------------------------') """


""" #While
cont = 0
n = int(input('Digite um numero:'))
while cont < 10:
  cont +=1
  m = cont * n
  print(f'{n} X {cont} = {m}')
print(f'Essa é a tabuada do {n}') """


""" print('tabuada do 3')
for x in range(1, 11):
    r = 5 * x
    print(f'5 x {x} = {r}') """

""" # sabado dia 04/fev
nome =('Café')
print(type(nome))


nome =('Café','Pao de Queijo')
print(type(nome))

nome =('Café','Pao de Queijo','bolo','mamão')
print(nome[1])

nome =('Café','Pao de Queijo','bolo','mamão')
print(type(nome[0]))
print(type(nome[1]))
print(type(nome[2])) """

""" nome =('Café','Pao de Queijo','bolo','mamão',10,5,True)
print(type(nome[0]))
print(type(nome[1]))
print(type(nome[2]))
print(type(nome[3]))
print(type(nome[4]))
print(type(nome[5]))
print(type(nome[6])) """

""" nome =['Café','Pao de Queijo','bolo','mamão',10,5,True]
print(type(nome[0]))
print(type(nome[1]))
print(type(nome[2]))
print(type(nome[3]))
print(type(nome[4]))
print(type(nome[5]))
print(type(nome[6])) """
""" nome =('Café','Pao de Queijo','bolo','mamão',10,5,True)
print(type(nome[0]))
print(type(nome[1]))
print(type(nome[2]))
print(type(nome[3]))
print(type(nome[4]))
print(type(nome[5]))
print(type(nome[6])) """
""" 
nome = [0,0,0,0,0]
for x in range(len(nome)):
  nome[x]=input('Nome do Aluno:') """
""" 
n = [0]*10
for x in range(len(n)):
    n[x]=input(f'Digite o {x}° numero: ')
for x in range(len(n)):
    print(n[x])   """

""" v =[0]*4
media = 0
for x in range(len(v)):
    v[x] = int(input(f'Digite a {x+1}° nota:'))
for x in range(len(v)):
    print(f'A nota {x+1} foi:{v[x]}')
    media = media + v[x]
print(f'A media é:{media/4}')  """

""" nome = ('cafe', 'pao de queijo','bolo')
print(type(nome))
nome = ['cafe','pao de queijo','bolo']
print(type(nome))
nome={'cafe':'acucar',
       'pao':'com queijo',
       'bolo':'chocolate'}
print(type(nome))
 """
""" 
 nome = {'primeiro':10,
        'segundo':50,
        'terceiro':8}
print(nome['segundo']) """


#--------------------------------------------------------
 #-----------------Funções---------------------------
""" def prifunc():
    print('Definindo com funções "def" em Python ')
prifunc()
prifunc()
prifunc()
prifunc()
prifunc()
prifunc()
prifunc()
prifunc() """

""" def prifunc():
   nome = 'Python'
   print(f'Definindo com funções "def" em {nome}!!!')
prifunc()
prifunc()
prifunc()
prifunc()
prifunc()
prifunc() """
""" 
def num(pnum, snum):
    print('Primeiro número: '+str(pnum)+'!!!')
    print('Segundo numero: '+str(snum)+'!!!')
    print('Soma: ',pnum + snum)
num(4, 8)
num(15, 45)
num(47, 18)
num(0, 87)
num(23, 65) """

def variacao(arg, *vartup):
    print("Primeiro argumento: ",arg)
    for item in vartup:
        print('O outro argumento: ',item)
    return
variacao(10)
variacao('Pão de QUeijo','Café')
variacao('Brincando','com os argumentos','seguindo mais ainda')