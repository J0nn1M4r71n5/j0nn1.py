n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))

# Use float quando tiver de esrever texto.
# O .1f serve para colocar apenas um algarismo depois do ponto (.). Se fosse dois algarismos seria .2f.