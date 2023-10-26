salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 1.5 / 100)
print('Um funcionário que ganhava R${:.2f}, com 1.5% de aumento, passa a receber R${:.2f}'.format(salário, novo))
