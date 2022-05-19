print(f'    SÓ PAR! \n\033[31m*faça o teste!*\033[m')
a1 = int(input('Valor do primeiro item: '))
a2 = a1 * 9
soma = a1 + a2
print(f'A soma entre {a1} e {a2} é igual a {soma}!')

if soma % 2 == 0:
    vd = True
else:
    vd = False

if vd:
    print('E o resultado é PAR!')
else:
    print('E o resultado é ÍMPAR!!')

print('Fun fact: o resultado sempre será par! KAKAS')
