class ProductInShop(object):
	name = 'product name'
	price = 0
	qnty = 1
	color = 'green'

	def __init__(self,one):
          self.sum = one

lego = ProductInShop(17)
lego.name = 'Lego Konstruktor'
lego.price = 15
lego.qnty = 10
lego.color = 'blue'

print lego.name, lego.price, lego.sum
print lego.__class__.__name__
"""
fisherprice = ProductInShop()
fisherprice.set_name('Igrushka Fisher Price')\
	.set_price(8).set_qnty(2).set_color('black')
"""
print