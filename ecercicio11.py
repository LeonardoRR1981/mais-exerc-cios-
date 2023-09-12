v = int(input('Qual o valor da compra? '))
p = (input('Pagamento a vista? (s), (n): '))
if (p == 's'):
    res = v * 0.95
    print('Sua compra e de R${:.2F} com o desconto de 5 por cento o pagamento a vista o total é R${:.2F}'.format(v, res))
elif (p == 'n'):
  div = input('Quantas vezes quer dividir? (3), (5) ou (10)? ')
  if (div == '3'):
    res2 = v
    print('Voce parcelou em {} vezes, cada parcela e de R${:.2f}, o total da compra e de R${:.2f}'.format(div,res2 / 3, res2 ))  
  elif (div == '5'):
    res3 = v * 0.02 + v
    print('Voce parcelou em {} vezes, cada parcela e de R${:.2f}, o total da compra e de R${:.2f}'.format(div, res3 / 5, res3))
  elif ( div == '10'):
    res4 = v * 0.08 + v
    print('Voce parcelou em {} vezes, cada parcela e de R${:.2f}, o total da compra e de R${:.2f}'.format(div, res4 / 10, res4))
