din = float(input('Digite quanto dinheiro voce tem na carteira: '))

dol = (din / 4.97)
print('Com R${} voce pode comprar US${:.2f}'.format(din,dol))