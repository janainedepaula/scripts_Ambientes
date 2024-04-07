#L01E09
#09. Escreva um programa que receba dois números e mostre qual deles é o maior. Teste com os valores 0.918259123 e 0.012412. 

a = input("Digite um número: ")
b = input("Digite outro número: ")

if a > b:
	print("Dentre os números digitados, o maior é: {} " .format(a))
else: 
	print("Dentre os números digitados, o maior é: {} " .format(b))