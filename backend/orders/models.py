from django.db import models

# Create your models here.
class Product(models.Model):

	public_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=150)	
	image = models.CharField(max_length=255)
	price = models.IntegerField()
	tax = models.IntegerField()

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		return f'({self.public_id}) {self.name}'

class Order(models.Model):

	first_name = models.CharField(max_length=65)
	last_name = models.CharField(max_length=65)
	email = models.EmailField(max_length=254)
	card_number = models.IntegerField()
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	total = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
