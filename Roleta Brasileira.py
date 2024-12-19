import random
print('Bem vindo a Roleta Brasileira')

Tiro = random.randint(1,6)
if Tiro == 1:
    Dano = 0
    print('Errou')
elif Tiro == 6:
    Dano = random.randint(25,30)
    print('Dano Critico')
else:
    Dano = random.randint(10,20)
    print('Acertou')
print(Tiro)
print(Dano)
#itens
'''Itens a serem usados'''
itens = ('Bandagem','Tala','Energetico','Capacete','Colete')
#print(itens)

#Menu
'''O menu tem q conter Inventario, Corpo, Inimigo, Restart, Sair'''
Menu = ['Inventario','Corpo','Inimigo','Restart']
#print(Menu)

#Inv
'''Vai conter os itens adquiridos podendo serem usados quando aberto o inventario'''
Inv = []
#print(Inv)

#Corpo/Inimigo
'''Mostra a parte do corpo onde foi acertado, quanto de vida essa parte ainda tem, corpo é constituido de cabeça,torax,abdomen,braços e pernas'''
Corpo = ['Cabeça','Torax','Braço Esq.','Abdomen','Braço Dir.','Perna Esq.','Perna Dir']
#print(Corpo)

#restart
'''Usado para reiniciar o jogo caso perca ou ganhe'''