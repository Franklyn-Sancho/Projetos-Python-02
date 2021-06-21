import random 

number = random.randint(1,10)

for i in range(0,3):
	user = int(input("advinhe o numero: "))
	if user == number:
		print("acertou")
		print(f"o numero é {number}")
		break
	elif user>number:
		print('Seu numero é maior')
	elif user < number:
		print("seu numero é menor")
else: 
	print(f"Boa tentativa, mais o numero é {number}")

