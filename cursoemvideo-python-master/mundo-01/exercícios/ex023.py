num = int(input('Informe um número com até 9 algarismos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
uM = num // 1000000 % 10
dM = num // 10000000 % 10
cM = num // 100000000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Unidade de Milhar: {}'.format(um))
print('Dezena de Milhar: {}'.format(dm))
print('Centena de Milhar: {}'.format(cm))
print('Unidade de Milhão: {}'.format(uM))
print('Dezena de Milhão: {}'.format(dM))
print('Centena de Milhão: {}'.format(cM))
