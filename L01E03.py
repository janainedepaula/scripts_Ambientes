#L01E3
'''
3. Escreva um programa que:
	a. Encontre a raiz quadrada de 25;
	b. Imprima o resultado de 2³;
	c. Some o quadrado de 3 com 2³;
	d. Imprima o resto de 7² pela raiz quadrada de 625;
'''

#a. Encontre a raiz quadrada de 25
print(25**(1/2))

#ou

from math import sqrt 
print(sqrt(25))


#b. Imprima o resultado de 2^3
print(2**3)

#c. Some o quadrado de 3 com 2³
print((3**2) + 2**3)

#ou

print(
	(3**2)
	+
	2**3)

#d. Imprima o resto de 7^2 pela raiz quadrada de 625
print((7**2) % (625**0.5)) 

#ou

print((7**2) % (625**(1/2)))
