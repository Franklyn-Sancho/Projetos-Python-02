name = str(input("Entre com seu Nick\n"))
print(
    f"Bem vindo, {name}. Você está andando pela floresta e de repente encontra um ogro.")
print(f"Você ainda não possui uma espada.")
print('1.Corre para encontrar uma arma 2.enfrenta o ogro')
user = int(input('Qual opção você escolhe?'))
if user == 1:
    print('Ufa! foi por pouco. Agora você precisa de dinheiro para comprar uma espada.')
    print('1.Fazer as missões 2.Encontrar dinheiro pela floresta')
    user = int(input('Qual opção você escolhe? '))
    if user == 1:
	    print('Ancião mestre: Bom dia, aventureiro. Preciso encontrar o mago abobrinha')
    elif user == 2:
	    print('Péssima decisão! agora terá que se arriscar pela floresta.')

elif user == 2:
    print('Você morreu')
else:
    print('Valor incorreto')

