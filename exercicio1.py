#Calculando o total a se pagar de aluguel de carro , dia = R$ 60,00 , KM = 0,15

km = int(input('Quantos KM o carro percorreu? '))
dias = int(input('Quantos dias ficou com o carro? '))
valor_km = km * 0.15
valor_dia = dias * 60 
print('O total a se pagar é R${}'.format(valor_dia + valor_km))