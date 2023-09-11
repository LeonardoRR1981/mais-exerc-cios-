m1 = int(input('Qual a nota da primeira materia? '))
m2 = int(input('Qual a nota da segunda materia? '))
m3 = int(input('Qual a nota da terceira materia? '))
mf = (m1 + m2 + m3) / 3
if ( mf >= 7):
    print('Sua nota final foi {} e vc passou de ano,'.format(mf))
elif (mf < 7):
    print('Sua nota final foi {} e vc não passou de ano, estude mais no proximo ano.'.format(mf))

