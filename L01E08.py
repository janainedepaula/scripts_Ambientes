#L1E08
#8. Desenvolva um programa que um valor em segundos e, em seguida, imprima quantas horas, minutos e segundos esse valor representa. Teste com o valor 300.

segundos = int(input("Digite um número: "))
minuto = segundos/60
horas = minuto/60

print("{} segundos são {} minutos ou {} horas!" .format(segundos, minuto, horas))