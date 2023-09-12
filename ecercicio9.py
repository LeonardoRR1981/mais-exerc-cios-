lado1 = int(input('Digite um valor: '))
lado2 = int(input('Digite um valor: '))
lado3 = int(input('Digite um valor: '))
if(lado1 == 0 and lado2 ==0 and lado3 == 0):
 if(lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1):
   print('Algo deu errado!!!!')
elif(lado1 == lado2 and lado2 == lado3):
   print('Triangulo Equilátero')
elif(lado1 != lado2 != lado3):
   print('Triangulo Escaleno')
else:
    print('Triangulo Isóceles')
  
