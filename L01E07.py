#L01E07
'''
7. Escreva um programa que receba três variáveis (a, b e c), com valores -4, 12 e 79, respectivamente, e determine se:
a) ((a>a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1))
b) ((a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)) and
(not(1>a**(1/2)))
'''
a=-4
b=12
c=79

#A.((a>a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1))
if ((a>a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)):
	print(True)
else:
	print(False)

#B ((a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)) and (not(1>a**(1/2)))
if ((a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)) and (not(1>a**(1/2))):
	print(True)
else: 
	print(False)