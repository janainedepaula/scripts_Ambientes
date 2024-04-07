#L01E11
#Escreva um programa em que calcule o diâmetro, a circunferência e a área de um círculo. O programa deve receber como entrada uma variável com o valor do raio. Considere Pi como 3,14. Teste com o valor 10.


raio = int(input("Qual o valor do raio? "))

Pi = 3.14
diametro = 2*raio
circunferencia = 2*Pi*raio 
area = Pi *(raio**2)

print("A área do círculo é {}, sua circuferência é de {} e seu diâmetro é {}!" .format(area, circunferencia, diametro))