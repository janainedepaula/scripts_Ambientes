#L01E13
#13. Escreva um programa que receba um número inteiro maior que zero e retorne se ele é par ou ímpar. 

numero=int(input("Digite um número"))
resto = numero % 2

if resto == 0:
	print ("O número digitado é par")
else: 
	print("O número digitado é impar")