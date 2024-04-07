#L01E12
#12. Escreva um programa que calcule o resultado de uma equação de segundo grau. Realize controle de exceções para verificar se delta é menor que zero.
#Equação de segundo grau: ax²+bx+c=0; delta: (b²-4ac); (-b±√(delta))/(2a). 

a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))

delta = (b**2) - 4 *(a*c)

if delta > 0:
    x1 = ((-b) - (delta**(0.5)))/(2*a)
    x2 = ((-b) + (delta**(0.5)))/(2*a)
    print("O valor de delta é: {}. Suas raízes reais são: x1= {} e x2= {}!" .format(delta, x1, x2))
elif delta == 0:
    print("O valor de delta é zero.")
else:
    print("Delta é negativo ({}), não possuindo raiz real." .format(delta))