#L01E04
'''
4. Escreva um programa que receba duas variáveis (a e b), com valores 10 e 7, respectivamente, e determine se:
a. a > b
b. (a * a) > b²
c. (b * a) <= a²
d. 2+5(a * a)-10 > a*b
'''

a = 10
b = 14


#A a > b ?
if a>b:
	print("Verdadeiro")
else:
	print("Falso")

#B (a * a) > b² ?
if (a*a)>b^2:
	print("Verdadeiro")
else:
	print("falso")

#C (b * a) <= a² ?
if (b*a)>= a**2:
	print("Verdadeiro")
else:
	print("Falso")

#D 2+5(a * a)-10 > a*b ?
if (2+5)*(a*a)-10 > a*b:
	print("Verdadeiro")
else:
	print("Falso")
