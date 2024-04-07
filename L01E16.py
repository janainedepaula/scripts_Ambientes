#L01E16
#16. Escreva um programa em Python que retorne o maior elemento da lista e sua posição.

#Para os exercícios 14-17, considere a seguinte lista:
numeros = [5,15,3,67,8,9,1,7,4,100,97,47,2,72]

maior_numero = max(numeros)
posicao = numeros.index(maior_numero) +1

print("O maior elemento presente na sequencia é " ,maior_numero, "e sua posição é" ,posicao,".")