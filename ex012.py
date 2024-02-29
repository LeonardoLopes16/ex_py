preco = float(input('Digite o preço do produto:'))


desc = preco*0.05
total = preco - desc

print('O valor do produto com desconto é de R${}:'.format(total))