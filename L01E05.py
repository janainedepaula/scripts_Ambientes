#L01E05
'''
5. Escreva um programa que receba três variáveis (a, b e c), com valores 10, 14 e 7, respectivamente, e determine se:
a) a > b and a*2 < c
b) a*5 < c**2 or a ==b
c) not(b >= c*2 and a <= c+3)
d) (a**2 < c **(1/2) and (a>b+c))
'''

a=10
b=14
c=7

#A. a > b and a*2 < c
if a>b and a*2<c:
	print("Verdadeiro")
else:
	print("Falso")

#B a*5 < c**2 or a ==b
if a*5<c**2 or a==b:
	print("a vezes 5 é menor que c ao quadrado ou a é igual a b")
else: 
	print("Um dos dois não é verdadeiro")

#C not(b >= c*2 and a <= c+3)
if not(b>=c*2 and a<=c+3):
	print("verdadeiro")
else:
	print("falso")

#D. (a**2 < c **(1/2) and (a>b+c)) 
if (a**2 < c **(1/2) and (a>b+c)):
	print("a ao quadrado é menor que c a meio e a é maior que b+c")
else:
	print("Uma ou nenhuma das condições são verdadeiras")

