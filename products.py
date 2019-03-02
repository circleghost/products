products = []

while True:
	name = input('輸入商品名稱：')
	if name == 'q':
		break
	price = input('輸入價格')
	price = int(price)
	products.append([name, price])

print(products)

for p in products:
	print(p[0], '價格是', p[1], '元')

with open('products.csv', 'w', encoding ='utf-8 ') as f:
	f.write('商品價格,名稱\n') 
	for p in products: 
		f.write(p[0] + ',' + str(p[1]) + '\n')