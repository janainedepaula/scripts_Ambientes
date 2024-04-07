#L01E17
#17. Escreva um programa em Python que retorne o menor elemento da lista e sua posição.

#Para os exercícios 14-17, considere a seguinte lista:
numeros = [5,15,3,67,8,9,1,7,4,100,97,47,2,72]

menor_numero = min(numeros)
posicao = numeros.index(menor_numero) +1

print("O menor elemento presente na sequencia é " ,menor_numero, "e sua posição é" ,posicao,".")
