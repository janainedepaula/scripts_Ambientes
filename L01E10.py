#L01E10
#10. Desenvolva um script que calcule o fatorial de um número. Teste com o número 5.

numero=int(input("Fatorial de "))

resultado=1
count=1

while count <= numero:
	resultado *= count 
	count += 1

print(resultado)