dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados?'))
pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.3f}'.format(pago,km))
