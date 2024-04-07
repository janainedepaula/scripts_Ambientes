#L01E06
'''
6. Agora, escreva um programa que receba três variáveis (a, b e c), com valores 18, 4 e 3, respectivamente, e determine se:
a) (a+b+c < a*c*b) or (1==1)
b) (a+b+c < a*c*b) and (1==1)
c) (a>a<b) and (not(a > b < a))
d) (a>a<b) or (not(a > b < a))
'''

a = 18
b = 4
c = 3

#A (a+b+c < a*c*b) or (1==1)
if (a+b+c) < (a*c)*b or (1==1):
	print("Pelo menos uma das condições é verdadeira")
else:
	print("Uma ou ambas condições são falsas")

#B (a+b+c < a*c*b) and (1==1)
if (a+b+c) < (a*c)*b and (1==1):
	print("Ambas condições são verdadeiras")
else:
	print("Pelo menos uma ou nenhuma das condições são verdadeiras")

#C (a>a<b) and (not(a > b < a))
if (a>a<b) and (not(a>b<a)):
	print("Ambas condições são verdadeiras")
else:
	print("Pelo menos um ou nenhuma das condições são verdadeiras")

#D (a>a<b) or (not(a > b < a))
if (a>a<b) or (not(a>b<a)):
	print("Uma ou ambas condições são verdadeiras")
else:
	print("Nenhuma das condições são verdadeiras")